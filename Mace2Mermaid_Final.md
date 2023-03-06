```mermaid
graph TD
A(Space):::classcolor 
B(Time):::classcolor 
C(Thunderstorm):::classcolor 
D(GeoPosition):::classcolor --> |subClassOf| A(Space)
E(FlightInformation):::classcolor 
F(RouteTrajectory):::classcolor --> |subClassOf| E(FlightInformation)
G(FlightRouteElement):::classcolor --> |subClassOf| F(RouteTrajectory)
H(4TrajectoryPointID):::classcolor --> |subClassOf| G(FlightRouteElement)
A(Space):::classcolor -->Ff{f}:::instancecolor
A(Space):::classcolor -->Gg{g}:::instancecolor
B(Time):::classcolor -->Hh{h}:::instancecolor
B(Time):::classcolor -->Ii{i}:::instancecolor
C(Thunderstorm):::classcolor -->Jj{j}:::instancecolor
D(GeoPosition):::classcolor -->Ff{f}:::instancecolor
D(GeoPosition):::classcolor -->Gg{g}:::instancecolor
E(FlightInformation):::classcolor -->Bb{b}:::instancecolor
E(FlightInformation):::classcolor -->Cc{c}:::instancecolor
E(FlightInformation):::classcolor -->Dd{d}:::instancecolor
E(FlightInformation):::classcolor -->Ee{e}:::instancecolor
F(RouteTrajectory):::classcolor -->Bb{b}:::instancecolor
F(RouteTrajectory):::classcolor -->Cc{c}:::instancecolor
F(RouteTrajectory):::classcolor -->Dd{d}:::instancecolor
F(RouteTrajectory):::classcolor -->Ee{e}:::instancecolor
G(FlightRouteElement):::classcolor -->Bb{b}:::instancecolor
G(FlightRouteElement):::classcolor -->Cc{c}:::instancecolor
G(FlightRouteElement):::classcolor -->Dd{d}:::instancecolor
H(4TrajectoryPointID):::classcolor -->Bb{b}:::instancecolor
H(4TrajectoryPointID):::classcolor -->Cc{c}:::instancecolor
Ee{e} -->|hasFlightRouteElement| Dd{d}:::instancecolor
Dd{d} -->|hasTrajectoryPoint| Bb{b}:::instancecolor
Dd{d} -->|hasTrajectoryPoint| Cc{c}:::instancecolor
Bb{b} -->|hasTime| Ii{i}:::instancecolor
Jj{j} -->|hasTime| Hh{h}:::instancecolor
Bb{b} -->|hasRoutePoint| Ff{f}:::instancecolor
Cc{c} -->|hasRoutePoint| Gg{g}:::instancecolor
Jj{j} -->|hasForcast| Ll{l}:::instancecolor
Jj{j} -->|hasAffectedArea| Kk{k}:::instancecolor
Ii{i} -->|TemporalConflict| Hh{h}:::instancecolor
Kk{k} -->|SpatialConflict| Ff{f}:::instancecolor
classDef instancecolor fill:#B73EE8
classDef classcolor fill:#F58420
```