# Deploy Log - Humedales Política Comparada

## 1. Objetivo Del Deploy

Publicar una aplicación Streamlit pedagógica sobre reglas legales, ruido de
datos y resultados de política pública.

El despliegue busca posicionar el proyecto como evidencia de un perfil hibrido:
ciencia política aplicada, ciencia de datos e inteligencia artificial agentica
orientada a prototipado técnico.

## 2. Estado Previo Del Proyecto

- App principal: `app.py`
- Branch de despliegue: `main`
- Runtime esperado: Python 3.12
- Plataforma objetivo: Streamlit Community Cloud
- Usuario GitHub: `dellacroce-NRC`
- Repositorio esperado: `dellacroce-NRC/humedales-politica-comparada`
- URL esperada: `https://github.com/dellacroce-NRC/humedales-politica-comparada`
- Ruta local actual: `C:\Users\nicol\.quickaccess-pins\Documentos\proyectos de datos\Humedales_Politica_Comparada`
- Fecha de preparación: 2026-05-19

## 3. Checklist Técnico Previo

| Item | Estado | Nota |
|---|---|---|
| `app.py` en raíz | OK | Entrypoint de Streamlit |
| Rutas absolutas | OK | La app genera datos sintéticos en memoria |
| `requirements.txt` | OK | Solo dependencias runtime |
| `requirements-dev.txt` | OK | Dependencias de pruebas locales |
| `.gitignore` | OK | Excluye cache, logs y entornos locales |
| Encoding textos UI | OK | Textos en español UTF-8 |
| Tests locales | OK | `4 passed` el 2026-05-19 |

## 4. Comandos Git Utilizados

El repositorio local tenía una metadata `.git` incompleta. Se limpió esa metadata
fallida y se reinicializó Git desde la carpeta actual:

```powershell
cd "C:\Users\nicol\.quickaccess-pins\Documentos\proyectos de datos\Humedales_Politica_Comparada"
git init
git branch -M main
git status
git add .
git commit -m "feat: initial architecture for legislative simulation"
git remote add origin https://github.com/dellacroce-NRC/humedales-politica-comparada.git
```

## 5. Creación Del Repositorio Remoto

El plugin de GitHub confirmó el usuario autenticado `dellacroce-NRC`, pero no
expone una herramienta directa para crear repositorios nuevos. Por eso la vía
principal será GitHub web.

### Opción Web

1. Ir a GitHub.
2. Crear repositorio público nuevo.
3. Owner: `dellacroce-NRC`.
4. Nombre: `humedales-politica-comparada`.
5. No agregar README, `.gitignore` ni licencia desde GitHub.
6. Crear el repositorio.

Luego ejecutar:

```powershell
git remote add origin https://github.com/dellacroce-NRC/humedales-politica-comparada.git
git push -u origin main
```

### Opción GitHub CLI

Si se instala `gh` en el futuro:

```powershell
gh auth login
gh repo create humedales-politica-comparada --public --source=. --remote=origin --push
```

## 6. Configuración Streamlit Cloud

- Repository: `dellacroce-NRC/humedales-politica-comparada`
- Branch: `main`
- Main file path: `app.py`
- App URL: `https://humedales-politica-comparada-m4ttyhxjplxfr2zk6e75ai.streamlit.app/`
- Fecha de despliegue: 2026-05-27
- Resultado: desplegada y verificada visualmente

## 7. Decisiones Tomadas

- Dataset sintético, no datos reales.
- Reglas legales simplificadas como clasificadores deterministas.
- Uso de Precision/Recall como traducción técnica de dilemas de política pública.
- Ruido de medición como simulación de datos municipales imperfectos.
- `pytest` se movió a `requirements-dev.txt` para mantener liviano el deploy.
- OpenAI Codex se usó como agente de implementación para acelerar arquitectura,
  código, visualizaciones, pruebas y documentación, manteniendo el criterio
  político-comparado bajo dirección humana.
- El README se reformuló como pieza de portafolio, no solo como manual técnico.

## 8. Limitaciones Conocidas

- No es un clasificador científico ni jurídico.
- No modela humedales reales.
- Las reglas comparadas son simplificaciones pedagógicas.
- La fidelidad legal puede aumentarse en una versión futura con fuentes
  normativas primarias.
- El uso de IA agentica no reemplaza validación experta; opera como apoyo de
  desarrollo y traducción técnica.

## 9. Incorporación Al Portafolio GitHub

- Repo nuevo: `humedales-politica-comparada`
- Tipo de acción: sumar como repositorio público nuevo
- Reemplazo de proyectos existentes: no aplica
- Eliminación de proyectos existentes: no aplica
- Confirmación manual en GitHub: completada
- Fecha de publicación: 2026-05-27

Nota: este proyecto no reemplaza ni elimina repositorios anteriores del
portafolio. Se publica como una pieza adicional para mostrar el perfil híbrido
del autor: ciencia política, ciencia de datos e inteligencia artificial
agentica.

## 10. Verificaciones Locales

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m pytest tests -q -p no:cacheprovider
python -m streamlit run app.py
```
