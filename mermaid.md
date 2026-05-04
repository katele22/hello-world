```mermaid
graph TD
    User((User)) --> Security[Spring Security]
    Security --> Controller[Spring MVC Controller]
    Controller --> Service[Business Service]
    Service --> DAO[Hibernate DAO]
    DAO --> MySQL[(MySQL 8)]
    
    Controller -.-> JSP[JSP View]
    JSP -.-> User
```
