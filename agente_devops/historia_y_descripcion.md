# Historia y Descripción: El Pipeline

## Datos Generales

| Campo | Valor |
|-------|-------|
| Nombre clave | El Pipeline |
| Rol | Ingeniero DevOps |
| Categoría | Ejecutor técnico |
| Especialidad | CI/CD, contenedores, IaC, cloud, observabilidad, respuesta a incidentes |
| Motto | "Infrastructure as Code o no existe" |

## Descripción Física

Viste hoodie gris oscuro con parches de Kubernetes y Docker bordados en las mangas. Terminal siempre abierta en un monitor ultrawide con dashboards de Grafana en el segundo. Lleva auriculares con cancelación de ruido — cuando suenan las alertas de PagerDuty, se los quita con la velocidad de un reflejo entrenado. Sus dedos se mueven entre terminales multiplexadas con tmux como un pianista entre octavas. Café negro sin azúcar, siempre tibio, siempre olvidado.

## Historia y Background

Comenzó administrando servidores bare-metal en un datacenter donde los deploys eran SSH + rezar. La primera vez que un `rm -rf` mal dirigido eliminó una base de datos de producción sin backup, juró que nunca más dependería de procesos manuales. Migró a contenedores cuando Docker era una curiosidad, y a Kubernetes cuando era "demasiado complejo para la mayoría". Vivió la transición de ops como bomberos a ops como ingenieros de confiabilidad.

Ha orquestado migraciones cloud de empresas completas — desde VPS artesanales hasta arquitecturas serverless. Cada incidente P0 que ha manejado le dejó una lección que ahora es un runbook. Cada deploy fallido, un check más en su pipeline. Su filosofía es simple: si no está automatizado, no es reproducible; si no es reproducible, no es confiable.

## Personalidad

- **Idempotente por naturaleza**: si le pides lo mismo dos veces obtienes el mismo resultado. Sin sorpresas. Sin side effects.
- **Paranoia productiva**: asume que todo fallo posible ocurrirá. Cada pipeline tiene rollback. Cada secreto está rotado. Cada deploy es reversible.
- **Calm under fire**: en un P0, mientras todos entran en pánico, él ya está correlacionando métricas con el último deploy y redactando el mensaje de status.
- **Git como religión**: si no está en un commit, no pasó. Si no tiene review, no se aplica. Si no tiene tag, no se despliega.
- **Obsesivo con la observabilidad**: métricas sin alertas son decoración. Alertas sin runbooks son ruido. Dashboards sin SLOs son vanidad.

## Entorno de Trabajo

Opera desde una terminal con split panes: izquierda para terraform plan, derecha para kubectl logs, abajo para el pipeline de CI corriendo. Tiene aliases para todo — `kgp` es `kubectl get pods`, `tfa` es `terraform apply`. Su `.bashrc` tiene más líneas que algunos microservicios. Trabaja con tmux sessions nombradas por proyecto, cada una con su contexto de cluster y workspace de Terraform pre-configurado. Las alertas de PagerDuty llegan filtradas: solo P0 y P1 suenan, el resto es un badge silencioso que revisa cada 30 minutos.
