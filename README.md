# Título del Proyecto

_Agente ADK con tool interna y externa (MCP)_

# Descripción

_Agente realizado con el framework Google ADK que se conecta con dos herramientas (tools), una tool local que devuelve los precios de los productos y otra tool externa que devuelve el listado de los productos (que se consume a través del protocolo MCP)._

## Instalación 🚀

_Instalamos Google Agent Development Kit (ADK)_
```
pip install google-adk
```

_Creamos un proyecto de agente_
```
adk create agent_product
```

_ingresamos el valor del GOOGLE_API_KEY en el archivo .env_
```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=
```

_Para acceder a las variable de entorno en el archivo .env instalamos_
```
pip install python-dotenv
```

_Ahora instalamos adk web para interactuar con el agente_
```
adk web
```

_Ingresamos la url http://127.0.0.1:8000 en el navegador. A través de esta interfaz podemos interactuar con los agentes que se hayan creado._
