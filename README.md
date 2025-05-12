# 🚀 DevSecOps Frontend Project: React + GitLeaks + OWASP ZAP

¡Bienvenido! Este proyecto es una demostración real de cómo implemento prácticas DevSecOps modernas en el desarrollo frontend. Aquí combino React, automatización CI/CD, análisis de seguridad y buenas prácticas de ingeniería para entregar software seguro y de calidad.

---

## 🌟 ¿Por qué es relevante este proyecto?

- **Automatización DevSecOps**: Seguridad integrada desde el primer commit hasta el despliegue.
- **Stack moderno**: React + Vite + Docker + GitHub Actions.
- **Pipeline completo**: Incluye SAST, DAST, SCA, escaneo de secretos y análisis de dependencias.
- **Documentación clara**: Cada paso está explicado para facilitar la colaboración y la auditoría.

---

## 🛠️ Tecnologías y Herramientas

- **Frontend**: React, Vite, Express
- **Seguridad**: GitLeaks, OWASP ZAP, Snyk, Trivy, CodeQL, Semgrep
- **CI/CD**: GitHub Actions
- **Contenedores**: Docker
- **Control de calidad**: ESLint, Prettier

---

## 📋 ¿Qué puedes ver en este repositorio?

1. **Detección automática de secretos** con GitLeaks y pre-commit hooks.
2. **Linter y formateo** con ESLint y Prettier.
3. **Pruebas y build automatizado** con GitHub Actions.
4. **Análisis de dependencias (SCA)** con Snyk y Dependency-Check.
5. **Análisis de seguridad estática (SAST)** con CodeQL y Semgrep.
6. **Verificación de licencias** de dependencias.
7. **Construcción y publicación de la imagen Docker** del frontend.
8. **Escaneo de vulnerabilidades en la imagen Docker** (Trivy, Snyk).
9. **Escaneo de seguridad dinámica (DAST)** con OWASP ZAP.
10. **Automatización de reportes y subida de artefactos** a GitHub.

---

## 🏗️ Estructura del Proyecto

```
gitleaks-report.json
README.md
setup_gitleaks.py
frontend/
  Dockerfile
  package.json
  server.js
  src/
    App.jsx
    ...
```

---

## 🚦 Pipeline DevSecOps: Workflows de GitHub Actions

Este repositorio implementa un pipeline CI/CD completo y seguro, orquestado con GitHub Actions y dividido en workflows reutilizables y modulares:

### 1. `build.yml` – Build y Test Frontend
- Instala dependencias, ejecuta linter, formatea el código y corre pruebas.
- Compila el frontend con Vite.
- Sube `node_modules` como artefacto para acelerar otros jobs.

### 2. `sca.yml` – Static Code Analysis (SCA)
- Usa Snyk para escanear vulnerabilidades en dependencias y subir resultados en formato SARIF.
- Ejecuta Dependency-Check para análisis adicional y sube reportes como artefactos.

### 3. `sast.yml` – Static Application Security Testing (SAST)
- Realiza análisis de seguridad estática con CodeQL (JavaScript).
- Ejecuta Semgrep con reglas OWASP y de seguridad, subiendo resultados a la pestaña de Security de GitHub.

### 4. `license-compliance.yml` – License Compliance
- Usa License Finder para verificar que las dependencias cumplen con licencias permitidas (MIT, Apache-2.0, BSD).
- Sube el reporte de licencias como artefacto.

### 5. `docker.yml` – Build Docker Image
- Construye y publica la imagen Docker del frontend en DockerHub.
- Usa variables de entorno para el nombre y versión de la imagen.

### 6. `container-image-scan.yml` – Scan Docker Image
- Escanea la imagen Docker con Trivy y Snyk para detectar vulnerabilidades.
- Sube los resultados a la pestaña de Security de GitHub.

### 7. `dast.yml` – Dynamic Application Security Testing (DAST)
- Despliega el frontend en un contenedor Docker.
- Ejecuta un escaneo DAST con OWASP ZAP sobre la app en ejecución.
- Permite la creación automática de issues si se detectan vulnerabilidades.
- Sube el reporte HTML como artefacto.

### 8. `main-pipeline.yml` – Orquestador Principal
- Orquesta todos los workflows anteriores en el orden correcto:
  1. Build
  2. SCA
  3. SAST
  4. License Compliance
  5. Docker Build
  6. Container Image Scan
  7. DAST
- Permite ejecución manual (`workflow_dispatch`) y en cada push a `main` (ignorando cambios en archivos de documentación).

---

## 🚀 ¿Cómo probarlo?

```bash
# 1. Instala dependencias y hooks de seguridad
python3 setup_gitleaks.py

# 2. Construye y ejecuta el frontend
cd frontend
docker build -t <usuario>/<nombre-imagen>:<versión> .
docker run -p 3000:3000 <usuario>/<nombre-imagen>:<versión>

# 3. Ejecuta el pipeline en GitHub Actions (push o PR)
```

---

## 👨‍💻 Sobre mí

Soy Juan Parra IV, ingeniero DevSecOps apasionado por la automatización, la seguridad y el desarrollo frontend moderno. Este proyecto es una muestra real de mi enfoque profesional y mis habilidades técnicas.

- [LinkedIn](https://www.linkedin.com/in/juanparraiv)
- [GitHub](https://github.com/JuanParraIV)

---

## 📄 Licencia

MIT

---

> ¡Gracias por visitar mi proyecto! Si buscas un perfil que combine desarrollo frontend, seguridad y automatización, ¡hablemos!
