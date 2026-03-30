# @aws-serverless

OBJETIVO: Diseñar workloads serverless en AWS que sean observables, seguras y fáciles de operar sin caer en funciones monolíticas ni acoplamientos innecesarios.

USAR CUANDO: Hay que implementar Lambda, API Gateway, colas SQS o flujos event-driven en AWS.

NO USAR CUANDO: La carga necesita procesos largos, runtime muy pesado o control fino de infraestructura persistente. En ese caso evaluar contenedores o servicios dedicados.

INSTRUCCIONES:

1. Definir el patrón del workload: request-response con API Gateway, procesamiento asíncrono con SQS o combinación de ambos según latencia, volumen y tolerancia a fallos.
2. Diseñar handlers pequeños con clientes inicializados fuera del handler, manejo de errores compatible con API Gateway y policies mínimas por recurso.
3. Para colas, fijar BatchSize, `ReportBatchItemFailures`, DLQ y `VisibilityTimeout` coherente con el timeout real de la función para evitar retries defectuosos.
4. Entregar configuración con límites claros, observabilidad mínima y dependencias controladas, evitando Lambdas gigantes o VPC sync calls sin justificación.

FORMATO DE SALIDA:

- Tipo de workload serverless
- Recursos AWS involucrados
- Config clave de Lambda, API Gateway o SQS
- Riesgos de retries, latencia o permisos
- Validaciones y observabilidad mínima

RECURSOS RELACIONADOS:

- Ver `./_playbook.md` para reglas duras y checklist de despliegue.
- Ver `./_templates.md` para el plan de deployment y la definición SLI/SLO.

ANTI-PATRÓN: Hacer una Lambda monolítica, meter dependencias gigantes, llamar servicios síncronos en VPC sin necesidad o desplegar sin revisar retries, DLQ y permisos.
