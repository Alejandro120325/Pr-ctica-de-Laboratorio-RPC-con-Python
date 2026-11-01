# 🚀 Práctica de Laboratorio: RPC con Python y Pyro4

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python)
![Pyro4](https://img.shields.io/badge/Pyro4-Distributed_Systems-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Completado-success?style=flat)

Este repositorio contiene la implementación práctica de un ecosistema de aplicaciones distribuidas utilizando el paradigma de **Llamadas a Procedimientos Remotos (RPC)** mediante la librería **Pyro4** en Python. 

El proyecto fue desarrollado como parte de la asignatura de **Sistemas Distribuidos** y se divide en 4 niveles de complejidad ascendente, abarcando desde conexiones directas hasta invocaciones asíncronas y manejo de estado.

---

## 👥 Colaboradores
* **Alejandro Ojeda** 
* **Adrian Castillo**

---

## 📂 Estructura del Proyecto

La práctica está organizada en 4 directorios independientes, cada uno representando un hito de aprendizaje:

* 🧮 **Nivel 1 (Calculadora Remota Básica):** Implementación de RPC sin Name Server. Conexión directa mediante el intercambio estático de URIs.
* 💬 **Nivel 2 (Sistema de Notificaciones):** Desacoplamiento de la arquitectura cliente-servidor introduciendo el *Name Server* de Pyro4 para un descubrimiento dinámico de servicios (`practica.mensajeria`).
* 🏦 **Nivel 3 (Banco Distribuido):** Gestión avanzada del estado (*Stateful Services*). Uso de la política de instancia `@Pyro4.behavior(instance_mode="session")` para mantener persistencia en los saldos de clientes concurrentes.
* ⏳ **Nivel 4 (Procesamiento Asíncrono):** Manejo de tareas pesadas sin bloqueo del hilo principal del cliente mediante el uso de futuros (`Pyro4.Future`), permitiendo ejecución paralela.

---

## ⚙️ Requisitos Previos

Asegúrate de tener instalado Python en tu sistema. Se recomienda el uso de un entorno virtual (`.venv`).

Instala la librería requerida ejecutando:
```bash
pip install Pyro4
```

---

## 🚀 Instrucciones de Ejecución

Para probar correctamente la arquitectura distribuida, es fundamental abrir múltiples terminales. 

### 1. Iniciar el Name Server (Obligatorio para Niveles 2, 3 y 4)
Abre una terminal dedicada y ejecuta el servidor de nombres de Pyro4. **Mantenla abierta** durante todas las pruebas:
```bash
pyro4-ns
```

### 2. Ejecutar un Nivel Específico
Elige el nivel que deseas probar. Por ejemplo, para ejecutar el **Nivel 3 (Banco Distribuido)**:

**Terminal A (Servidor):**
```bash
python "Nivel 3\nivel3_servidor.py"
```

**Terminal B (Cliente):**
```bash
python "Nivel 3\nivel3_cliente.py"
```
*(Puedes abrir múltiples terminales de cliente simultáneas para comprobar el manejo de sesiones independientes).*

---

## 🧠 Conceptos Teóricos Aplicados

Durante el desarrollo de esta práctica se aplicaron los siguientes conceptos clave en sistemas distribuidos:
1. **Transparencia de ubicación** mediante Name Servers.
2. **Serialización segura** utilizando `serpent` (reemplazo de `pickle` para mitigar vulnerabilidades de inyección de código).
3. Diferenciación entre **servicios Stateful (con estado)** y **Stateless (sin estado)**.
4. Concurrencia y **callbacks asíncronos** en peticiones de red intensivas.

---
*Desarrollado para la Universidad Politécnica Salesiana - Sede Quito (Ecuador)* 🇪🇨
