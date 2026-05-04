%% graph TD
%%     subgraph Client_Layer [View - JSP]
%%         A[Browser/User] -->|HTTP Request| B(JSTL/HTML Templates)
%%     end

%%     subgraph Spring_Framework [Controller & Security]
%%         B -->|Form Data| C{Spring Security Bouncer}
%%         C -->|Authorized| D[MVC Controllers]
%%     end

%%     subgraph Business_Layer [Service Layer]
%%         D --> E[Business Services]
%%     end

%%     subgraph Persistence_Layer [Hibernate ORM]
%%         E --> F[DAO - Data Access Objects]
%%         F --> G[SessionFactory Singleton]
%%         G --> H[(MySQL Database)]
%%     end

%%     style G fill:#f9f,stroke:#333,stroke-width:2px
%%     style C fill:#fff4dd,stroke:#d4a017

graph TB
    subgraph Client_Layer [Client Layer]
        Browser[Web Browser]
    end

    subgraph Presentation_Layer [Presentation Layer - Spring MVC]
        JSP[JSP Files + JSTL]
        Jasper[Tomcat Jasper Engine]
        Controller[Spring MVC Controllers]
    end

    subgraph Security_Layer [Security Layer - Spring Security]
        FilterChain[Security Filter Chain]
        AuthManager[Authentication Manager]
    end

    subgraph Business_Layer [Business Layer]
        Service[Service Classes]
    end

    subgraph Persistence_Layer [Persistence Layer - Hibernate ORM]
        DAO[DAO Implementation]
        SFB[LocalSessionFactoryBean]
        Session[Hibernate Session]
        Entities[JPA Entities / Models]
    end

    subgraph Data_Layer [Database Layer]
        MySQL[(MySQL 8.0 Database)]
    end

    %% Flow Connections
    Browser <--> FilterChain
    FilterChain <--> Controller
    Controller <--> Service
    Service <--> DAO
    DAO <--> Session
    Session <--> SFB
    SFB <--> Entities
    Session <--> MySQL
    
    %% View Rendering
    Controller -.-> Jasper
    Jasper -.-> JSP
    JSP -.-> Browser

    %% Styling
    style Client_Layer fill:#f9f,stroke:#333,stroke-width:2px
    style Security_Layer fill:#ff9,stroke:#333,stroke-width:2px
    style Persistence_Layer fill:#bbf,stroke:#333,stroke-width:2px
    style Data_Layer fill:#dfd,stroke:#333,stroke-width:2px
