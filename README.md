# Fasal-AI 🌾 — Multi-Agent Agricultural Advisory & Export Intelligence

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/Agent%20Framework-CrewAI-red.svg)](https://www.crewai.com/)
[![OpenAI GPT-4o](https://img.shields.io/badge/LLM-OpenAI%20GPT--4o-green.svg)](https://openai.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/Orchestration-LangChain-orange.svg)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent, multi-agent AI agricultural advisory and export compliance ecosystem designed to empower farmers and agribusinesses with actionable agronomic intelligence, real-time crop disease diagnostics, hyper-local weather alerts, international export compliance (MRL/PSQCA), and localized multilingual guidance (Urdu, Punjabi, Sindhi, and English).

---

## 📌 Table of Contents

- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Multi-Agent Swarm Overview](#-multi-agent-swarm-overview)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage & Running](#-usage--running)
  - [1. Streamlit Web Dashboard](#1-interactive-streamlit-web-dashboard)
  - [2. Orchestrator Pipeline (CLI)](#2-orchestrator-pipeline-cli)
- [Export Compliance & Standards](#-export-compliance--standards)
- [Contributors & Credits](#-contributors--credits)

---

## 🌟 Key Features

- **🔬 Vision-Based Crop Disease Diagnostics**: Instant identification of plant pathogens and physiological conditions using Plant.id API and GPT-4 Vision, delivering confidence percentages, disease stages, and immediate treatments.
- **🌦️ Proactive Micro-Climate Advisories**: Dynamic weather forecasting synchronized with irrigation schedules to prevent fungal outbreaks, frost damage, and fertilizer runoff.
- **🌱 Smart Agronomy & Yield Optimization**: Precision fertilizer calculations (NPK, Urea, DAP) matched against soil texture, acreage, crop phenological stage, and projected yield estimates.
- **🚢 Export Compliance & MRL Auditing**: Pre-harvest compliance verification against international standards (UAE, EU, GCC, PSQCA) checking pesticide Maximum Residue Limits (MRL) and pre-harvest intervals (PHI).
- **🗣️ Multilingual & Farmer-First Communication**: Localized advisory synthesis tailored in **Urdu (اردو)**, **Punjabi (پنجابی)**, **Sindhi (سنڌي)**, and **English**, structured for easy delivery via SMS and WhatsApp.

---

## 🏗️ System Architecture

```
                                  [ Farmer / Agribusiness User ]
                                                 │
                                                 ▼
                             ┌───────────────────────────────────────┐
                             │       Streamlit Web Dashboard /       │
                             │       CLI Orchestrator Pipeline       │
                             └──────────────────┬────────────────────┘
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 │                                                             │
                 ▼                                                             ▼
     [ Crop Image Input ]                                            [ Crop & Farm Profile ]
                 │                                                             │
                 ▼                                                             ▼
    ┌─────────────────────────┐                                   ┌─────────────────────────┐
    │     1. Vision Agent     │                                   │    2. Weather Agent     │
    │  (Plant.id + Vision LLM)│                                   │ (Real-time Agro Forecast│
    └────────────┬────────────┘                                   └────────────┬────────────┘
                 │                                                             │
                 └──────────────────────────────┬──────────────────────────────┘
                                                │
                                                ▼
                                   ┌─────────────────────────┐
                                   │   3. Agronomy Agent     │
                                   │ (Fertilizer, Yield Pred,│
                                   │   Soil-Crop Management) │
                                   └────────────┬────────────┘
                                                │
                                                ▼
                                   ┌─────────────────────────┐
                                   │ 4. Export Compliance    │
                                   │ (MRL Checks, PSQCA,     │
                                   │   International Stds)   │
                                   └────────────┬────────────┘
                                                │
                                                ▼
                                   ┌─────────────────────────┐
                                   │   5. Language Agent     │
                                   │ (Urdu / Punjabi / Sindhi│
                                   │   WhatsApp/SMS Format)  │
                                   └────────────┬────────────┘
                                                │
                                                ▼
                                   [ Actionable Advisory Report ]
```

---

## 🤖 Multi-Agent Swarm Overview

| Agent | Responsibility | Core Tools & Models |
|---|---|---|
| **Vision Diagnostics Agent** | Analyzes crop leaves, lesions, and symptoms; determines disease classification and confidence score. | Plant.id API, GPT-4 Vision, PIL |
| **Weather Intelligence Agent** | Evaluates precipitation risk, relative humidity, wind speed, and formulates proactive farm warnings. | Open-Meteo / Weather Tools, LLM Reasoner |
| **Agronomy Specialist Agent** | Delivers customized dosage for fertilizers, soil amendments, and predicts harvest yield per acre. | Agronomy Knowledge Base, Crop Stage Matrices |
| **Export Compliance Agent** | Audits chemical applications (Chlorpyrifos, Imidacloprid, etc.) against target export markets and MRL safety limits. | MRL Database, PSQCA Guidelines, International Standards |
| **Language & Delivery Agent** | Translates technical insights into farmer-friendly vernacular and creates clean bullet points for WhatsApp / SMS. | Multilingual Prompt Engine, Urdu/Punjabi Lexicon |

---

## 💻 Tech Stack

- **Agent Orchestration**: [CrewAI](https://www.crewai.com/) & [LangChain](https://www.langchain.com/)
- **Large Language Models**: OpenAI GPT-4o & GPT-4o-mini
- **Computer Vision**: [Plant.id API](https://plant.id/) + OpenAI GPT-4 Vision
- **User Interface**: [Streamlit](https://streamlit.io/)
- **Vector & Data Stores**: [ChromaDB](https://www.trychroma.com/), JSON Knowledge Bases
- **Language & Runtime**: Python 3.10+, Requests, Pillow, python-dotenv

---

## 📂 Repository Structure

```
FasalAI/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── vision_agent.py             # Crop image disease diagnostics
│   │   ├── weather_agent.py            # Micro-climate agro advisories
│   │   ├── agronomy_agent.py           # Fertilizer & yield prediction
│   │   ├── export_compliance_agent.py  # MRL & PSQCA export verification
│   │   └── language_agent.py           # Vernacular localization & output
│   ├── tools/
│   │   ├── weather_tool.py             # Live weather queries
│   │   ├── plant_id_tool.py            # Plant.id API interface
│   │   └── mrl_checker_tool.py         # MRL threshold evaluator
│   ├── data/
│   │   ├── crop_knowledge.json         # Crop growth cycles & recommendations
│   │   ├── mrl_database.json           # Country-specific chemical limits
│   │   └── psqca_standards.json        # Pakistan standards & export guidelines
│   ├── app.py                          # Streamlit web application frontend
│   └── main.py                         # Complete 5-agent pipeline runner
├── .env.example                        # API keys template
├── .gitignore                          # Git ignore rules
├── requirements.txt                    # Project dependencies
├── main.py                             # Root key validator entry point
├── app.py                              # Root app launcher
└── README.md                           # Documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher installed
- Valid API keys:
  - [OpenAI API Key](https://platform.openai.com)
  - [Plant.id API Key](https://plant.id) (Free tier available)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hateeemkhann/FasalAI.git
   cd FasalAI
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Copy the template environment file and add your secret API keys:

```bash
# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Open `.env` in your text editor and fill in your keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
PLANT_ID_API_KEY=your_plant_id_api_key_here
```

---

## 🖥️ Usage & Running

### 1. Interactive Streamlit Web Dashboard

Launch the web interface for disease scanning, interactive agronomy consultation, and real-time weather analytics:

```bash
streamlit run src/app.py
```

### 2. Orchestrator Pipeline (CLI)

Run the automated end-to-end multi-agent pipeline on sample agricultural scenarios:

```bash
python src/main.py
```

---

## 🌐 Export Compliance & Standards

Fasal-AI bridges local agricultural practice with global export requirements by auditing:
- **Maximum Residue Limits (MRL)** for key export crops (Rice, Wheat, Mango, Citrus, Cotton).
- **Target Market Guidelines**: UAE Ministry of Climate Change & Environment, European Commission Food Safety, and GCC food standards.
- **PSQCA Harmonization**: Ensuring compliance with Pakistan Standards and Quality Control Authority.

---

## 👥 Contributors & Credits

- **Muhammad Hateem Khan** ([@hateeemkhann](https://github.com/hateeemkhann)) — Core Contributor & Project Implementation
- **Absar Anwer** ([@absar-1](https://github.com/absar-1)) — Collaborator & Co-Creator

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
