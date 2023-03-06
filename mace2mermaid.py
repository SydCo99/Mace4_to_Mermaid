import re

def mace2mermaid(mace_input, owl_file):

    owl_file_name = owl_file
    f = open(f"{owl_file_name}", "r")
    owl_lines = f.read()
    owl_lines = re.split(" \.", owl_lines)

    new_owl_lines = []
    for line in owl_lines: 
        new_line = line.strip().replace('\n', '')
        new_owl_lines.append(new_line)
    object_properties = []
    classes = []
    for i in range(len(new_owl_lines)):
        if "rdf:type owl:ObjectProperty" in new_owl_lines[i]:
            object_properties.append(new_owl_lines[i])
        if "rdf:type owl:Class" in new_owl_lines[i]:
            classes.append(new_owl_lines[i])
    class_and_subclass = []

    for i in range(len(classes)):
        if "rdfs:subClassOf" in classes[i]:
            root = classes[i].partition("<http://example.com/")[2].partition(">")[0].strip()
            subclass = classes[i].partition("rdfs:subClassOf <http://example.com/")[2].partition(">")[0].strip()
            class_and_subclass.append(f"root = {root}, subclass_of = {subclass}")
    def find_subclass(test_str):
        for i in range(len(class_and_subclass)):
            if f"root = {test_str}" in class_and_subclass[i]:
                return class_and_subclass[i].partition("subclass_of = ")[2].strip()
    label_lookup = []
    for i in range(len(object_properties)):
        label = object_properties[i].partition("rdfs:label ")[2].partition("@en")[0].strip()
        uri = object_properties[i].partition("<http://example.com/")[2].partition(">")[0].strip()
        label_lookup.append((f"{label}, {uri}"))

    def object_prop_label(input_str):
        for i in range(len(label_lookup)):
            if input_str in label_lookup[i]:
                value = (label_lookup[i].partition(" ")[0].partition(",")[0].strip())
                value = value.replace('"', '')
                return value
            
    label_lookup_classes = []
    for i in range(len(classes)):
        label = classes[i].partition("rdfs:label ")[2].partition("@en")[0].strip()
        uri = classes[i].partition("<http://example.com/")[2].partition(">")[0].strip()
        label_lookup_classes.append((f"{label}, {uri}"))

    def class_label(input_str):
        for i in range(len(label_lookup_classes)):
            if input_str in label_lookup_classes[i]:
                value = (label_lookup_classes[i].partition(" ")[0].partition(",")[0].strip())
                value = value.replace('"', '')
                return value


    file_name = mace_input
    f = open(f"{file_name}", "r")
    lines = f.read()
    full_list = lines.split('\n')
    domain_size_full = []
    for i in range(len(full_list)):
        if "domain size" in full_list[i]:
            domain_size_full.append(full_list[i])
    temp = re.findall(r'\d+', domain_size_full[0])
    domain_size = list(map(int, temp))
    domain_size = domain_size[0]
    constants = []
    for i in range(len(full_list)):
        if "function" in full_list[i]:
            constants.append(full_list[i])

    class_instances = []
    for i in range(len(full_list)):
        if "(_)" in full_list[i]:
            class_instances.append(full_list[i])
    instance_relations = []
    for i in range(len(full_list)):
        if "(_,_)" in full_list[i]:
            for counter in range(domain_size):
                instance_relations.append(full_list[i+counter])
                        
    instance_relations_final = [instance_relations[n:n+domain_size] for n in range(0, len(instance_relations), domain_size)]

    characters = ["",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(len(class_instances)):
        class_instances[i] = class_instances[i].lower()

    class_types_finished = []
    for i in range(len(class_instances)): 
        class_type = class_instances[i].partition("(")[2].partition("(")[0].strip()
        letter = characters[i +1].upper()
        class_type = class_type.lower()
        subclass = find_subclass(class_type)
        class_type_final = class_label(class_type)

        if subclass is None: 
            class_types_finished.append((f"{letter}({class_type_final}):::classcolor "))
        else: 
            for c in range(len(class_instances)):   
                if subclass in class_instances[c]: 
                    subclass_letter = (characters[c+1].upper())
            class_types_finished.append(f"{letter}({class_type_final}):::classcolor --> |subClassOf| {subclass_letter}({class_label(subclass)})")

    instance_list = []
    for i in range(len(class_instances)):
        instances = class_instances[i].partition(", ")[2].partition("),")[0].strip()
        instance_list.append(instances)

    new_instance_list = []
    for i in range(len(instance_list)):
        new_instance_list.append(instance_list[i].strip('][').split(', '))

    
    class_instances_without_subclasses = []
    for i in range(len(class_instances)): 
        class_type = class_instances[i].partition("(")[2].partition("(")[0].strip()
        class_type_final = class_label(class_type)

        letter = characters[i +1].upper()
        class_instances_without_subclasses.append((f"{letter}({class_type_final}):::classcolor "))

    class_instances_finished = []
    for i in range(len(new_instance_list)):
        class_type_name = class_instances_without_subclasses[i] + "-->"
        for c in range(len(new_instance_list[i])):
            if "1" in new_instance_list[i][c]:
                instance_letter = (c + 1)
                letter_rep = characters[int(instance_letter)]
                instance_full = (f"{letter_rep.upper()}{letter_rep.lower()}" + "{" + letter_rep + "}:::instancecolor")
                class_instances_finished.append(class_type_name + instance_full)

    instance_relations_for_print = []
    for i in range(len(instance_relations_final)):  
        for c in range(domain_size):
            if "1," in instance_relations_final[i][c]:
                relation_name = instance_relations_final[i][0].partition("(")[2].partition("(")[0].strip()
                relation_name = relation_name.lower()
                relation_label = (object_prop_label(relation_name))
                list_for_counts = [int(x) for x in instance_relations_final[i][c].split(',') if x.strip().isdigit()]
                if sum(list_for_counts) > 1: 
                    for x in range(len(list_for_counts)):  
                        if list_for_counts[x] == 1:
                            column_rep = characters[x + 1]
                            row_rep = characters[c]
                            instance_relations_for_print.append(f"{row_rep.upper()}{row_rep.lower()}" + "{" + row_rep + "}" + f" -->|{relation_label}| " + f"{column_rep.upper()}{column_rep.lower()}" + "{" + column_rep + "}:::instancecolor")
                else:
                    for x in range(len(list_for_counts)):  
                        if list_for_counts[x] == 1:
                            column_rep = characters[x + 1]
                            row_rep = characters[c]
                            instance_relations_for_print.append(f"{row_rep.upper()}{row_rep.lower()}" + "{" + row_rep + "}" + f" -->|{relation_label}| " + f"{column_rep.upper()}{column_rep.lower()}" + "{" + column_rep + "}:::instancecolor")
            
    with open(f'Mace2Mermaid_Final.md', 'w') as fp:
        fp.write("```mermaid\n")
        fp.write("graph TD\n")
        fp.write('\n'.join([''.join(i) for i in class_types_finished]))
        fp.write('\n')
        fp.write('\n'.join([''.join(i) for i in class_instances_finished]))
        fp.write('\n')
        fp.write('\n'.join([''.join(i) for i in instance_relations_for_print]))
        fp.write("\nclassDef instancecolor fill:#B73EE8\nclassDef classcolor fill:#F58420")
        fp.write('\n')
        fp.write('```')


mace2mermaid("Mace4_Trimmed", "raw_owl.owl")