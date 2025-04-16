import os
from PIL import Image
from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

def selecionar_arquivos(titulo, tipos, multiplos=False):
    root = Tk()
    root.withdraw()  # Oculta a janela principal
    if multiplos:
        arquivos = filedialog.askopenfilenames(title=titulo, filetypes=tipos)
    else:
        arquivos = filedialog.askopenfilename(title=titulo, filetypes=tipos)
    return arquivos

def imagens_para_pdf(imagens_paths, saida_pdf):
    imagens_rgb = []

    for path in imagens_paths:
        if not os.path.exists(path):
            print(f"Imagem não encontrada: {path}")
            return False
        img = Image.open(path).convert('RGB')
        imagens_rgb.append(img)

    if imagens_rgb:
        imagens_rgb[0].save(saida_pdf, save_all=True, append_images=imagens_rgb[1:])
        return True
    return False

def juntar_pdfs(pdf1_path, pdf2_path, pdf_saida_path):
    if not os.path.exists(pdf1_path) or not os.path.exists(pdf2_path):
        print("Um dos arquivos PDF não foi encontrado.")
        return False

    merger = PdfMerger()
    merger.append(pdf1_path)
    merger.append(pdf2_path)
    merger.write(pdf_saida_path)
    merger.close()
    return True

# === INTERAÇÃO COM O USUÁRIO ===
print("Selecione as imagens (JPG/PNG)...")
imagens = selecionar_arquivos("Selecione as imagens", [("Imagens", "*.jpg *.jpeg *.png")], multiplos=True)

if not imagens:
    print("❌ Nenhuma imagem selecionada.")
    exit()

print("Selecione o PDF existente...")
pdf_existente = selecionar_arquivos("Selecione o PDF", [("PDF", "*.pdf")])

if not pdf_existente:
    print("❌ Nenhum PDF selecionado.")
    exit()

# Caminhos dos arquivos temporários/saída
pdf_imagens = "imagens_convertidas.pdf"
pdf_final = "pdf_final.pdf"

# Processamento
if imagens_para_pdf(imagens, pdf_imagens):
    if juntar_pdfs(pdf_imagens, pdf_existente, pdf_final):
        print("✅ PDF final criado com sucesso:", os.path.abspath(pdf_final))
    else:
        print("❌ Falha ao juntar os PDFs.")
else:
    print("❌ Falha ao converter imagens para PDF.")
