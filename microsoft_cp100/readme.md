## ✅ **Fluxo sugerido no Azure ML Studio**

### 🔹 **1. Dataset de entrada**
- **Bloco:** `Import Data`  
  📌 Conecte o arquivo `.csv` ou dataset já presente no workspace.

---

### 🔹 **2. Selecionar as colunas relevantes**
- **Bloco:** `Select Columns in Dataset`  
  ✅ Escolha apenas as colunas que deseja usar como variáveis explicativas e a variável-alvo.  
  ⚠️ **Não inclua colunas como IDs ou textos irrelevantes.**

---

### 🔹 **3. Dividir os dados**
- **Bloco:** `Split Data`  
  📌 Parâmetros sugeridos:
  - Fração para treino: **0.7** (ou seja, 70% treino / 30% teste)
  - Divisão baseada em amostragem aleatória

---

### 🔹 **4. Treinar o modelo**
- **Bloco:** `Train Model`  
  - Conecte a saída de treino do `Split Data` aqui.
  - Selecione a **coluna alvo (target)** ao configurar o bloco.

#### ➕ Use um dos seguintes algoritmos antes desse passo:
- `Two-Class Logistic Regression`
- `Two-Class Decision Forest`
- `Two-Class SVM`
- etc.

---

### 🔹 **5. Pontuar os dados de teste**
- **Bloco:** `Score Model`  
  - Entrada 1: Modelo treinado (saída do `Train Model`)
  - Entrada 2: Dados de teste (saída do `Split Data`)

---

### 🔹 **6. Avaliar o modelo**
- **Bloco:** `Evaluate Model`  
  - Conecte a saída do `Score Model` aqui para visualizar métricas como AUC, Accuracy, Precision, etc.

---

## 🧩 Fluxo Visual (Resumo)

```
Import Data
     ↓
Select Columns in Dataset
     ↓
Split Data
   ↙      ↘
Train    → Score Model → Evaluate Model
Model
```

---

### 💡 Dicas Extras:

- **Para garantir compatibilidade no Score Model:**
  - Use `Select Columns in Dataset` **antes do Score Model**, também nos dados de teste.
  - Isso força os dados de teste a terem **as mesmas features usadas no treino**.





