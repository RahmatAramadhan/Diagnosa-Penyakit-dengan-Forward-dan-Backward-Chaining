import tkinter as tk
from tkinter import messagebox
import re;

knowledge_base = {
    'influenza': {'demam', 'batuk', 'pilek', 'sakit tenggorokan', 'kelelahan'},
    'diabetes tipe 2': {'sering haus', 'sering buang air kecil', 'kelelahan', 'penglihatan kabur', 'luka yang lama sembuh'},
    'hipertensi': {'sakit kepala', 'sesak napas', 'mimisan', 'kelelahan', 'nyeri dada'},
    'gagal jantung': {'sesak napas', 'kelelahan', 'pembengkakan kaki', 'detak jantung cepat', 'nyeri dada'},
    'pneumonia': {'demam', 'batuk', 'sesak napas', 'nyeri dada', 'kelelahan'},
    'asma': {'sesak napas', 'mengi', 'batuk', 'dada terasa sempit', 'sesak napas pada malam hari'},
    'tbc': {'batuk berkepanjangan', 'demam', 'berkeringat malam hari', 'penurunan berat badan', 'kelelahan'},
    'hepatitis': {'kuning pada kulit dan mata', 'demam', 'kelelahan', 'nyeri perut', 'mual'},
    'gastritis': {'nyeri perut', 'mual', 'muntah', 'perut kembung', 'kehilangan nafsu makan'},
    'radang sendi': {'nyeri sendi', 'pembengkakan sendi', 'kekakuan sendi', 'kelelahan', 'penurunan fungsi sendi'},
    'anemia': {'kelelahan', 'pusing', 'sesak napas', 'kulit pucat', 'detak jantung cepat'},
    'migrain': {'sakit kepala berat', 'mual', 'muntah', 'sensitivitas cahaya', 'sensitivitas suara'},
    'depresi': {'kehilangan minat', 'perasaan sedih', 'perubahan nafsu makan', 'kelelahan', 'sulit tidur'},
    'bipolar': {'perubahan mood ekstrem', 'euforia', 'depresi', 'kehilangan energi', 'kesulitan konsentrasi'},
    'skizofrenia': {'halusinasi', 'delusi', 'pemikiran kacau', 'kehilangan motivasi', 'perubahan pola tidur'},
    'ocd': {'obsesi', 'kompulsi', 'kecemasan', 'perilaku berulang', 'kehilangan waktu produktif'},
    'ptsd': {'flashback', 'mimpi buruk', 'kecemasan', 'depresi', 'menghindari situasi tertentu'},
    'stroke': {'mati rasa di wajah', 'kesulitan berbicara', 'kelemahan pada satu sisi tubuh', 'penglihatan kabur', 'kehilangan keseimbangan'},
    'parkinson': {'tremor', 'kekakuan otot', 'gerakan lambat', 'gangguan postur', 'kesulitan menulis'},
    'alzheimer': {'kehilangan memori', 'kebingungan', 'kesulitan berbicara', 'perubahan kepribadian', 'kesulitan menyelesaikan tugas sehari-hari'},
    'bronkitis': {'batuk berdahak', 'sesak napas', 'demam', 'kelelahan', 'nyeri dada'},
    'penyakit paru obstruktif kronis (ppok)': {'sesak napas', 'batuk berkepanjangan', 'produksi lendir berlebih', 'kelelahan', 'infeksi saluran pernapasan sering'},
    'infeksi saluran kemih (isk)': {'nyeri saat buang air kecil', 'sering buang air kecil', 'nyeri perut bawah', 'urin berwarna gelap', 'demam'},
    'kanker payudara': {'benjolan di payudara', 'perubahan ukuran payudara', 'perubahan kulit payudara', 'keluarnya cairan dari puting', 'nyeri payudara'},
    'kanker paru': {'batuk berkepanjangan', 'darah dalam dahak', 'sesak napas', 'penurunan berat badan', 'nyeri dada'},
    'kanker prostat': {'kesulitan buang air kecil', 'darah dalam urin', 'nyeri punggung bawah', 'disfungsi ereksi', 'kelemahan pada kaki'},
    'kanker kolorektal': {'perubahan kebiasaan buang air besar', 'darah dalam tinja', 'nyeri perut', 'penurunan berat badan', 'kelelahan'},
    'kanker hati': {'kuning pada kulit dan mata', 'nyeri perut', 'penurunan berat badan', 'kelelahan', 'pembengkakan perut'},
    'demam berdarah': {'demam tinggi', 'nyeri sendi', 'nyeri otot', 'ruam kulit', 'kelelahan'},
    'malaria': {'demam berkala', 'menggigil', 'berkeringat', 'nyeri otot', 'mual'},
    'demam tifoid': {'demam tinggi', 'sakit kepala', 'nyeri perut', 'diare', 'kelelahan'},
    'cacar air': {'ruam kulit berbintik', 'demam', 'kelelahan', 'gatal', 'sakit kepala'},
    'campak': {'ruam kulit', 'demam', 'batuk', 'pilek', 'mata merah'},
    'rubella': {'ruam kulit', 'demam', 'nyeri sendi', 'pembengkakan kelenjar getah bening', 'kelelahan'},
    'gondongan': {'pembengkakan kelenjar ludah', 'demam', 'nyeri saat mengunyah', 'kelelahan', 'sakit kepala'},
    'sinusitis': {'nyeri wajah', 'pilek', 'demam', 'kelelahan', 'bau mulut'},
    'alergi': {'gatal-gatal', 'ruam kulit', 'bersin', 'mata berair', 'pilek'},
    'kudis': {'gatal parah', 'ruam kulit', 'luka gatal', 'kerak kulit', 'kemerahan'},
    'eksim': {'gatal kulit', 'kulit kering', 'ruam merah', 'kerak kulit', 'pembengkakan kulit'},
    'psoriasis': {'plak kulit merah', 'gatal', 'kulit bersisik', 'nyeri sendi', 'kuku menebal'},
    'hiv/aids': {'demam', 'kelelahan', 'pembengkakan kelenjar getah bening', 'penurunan berat badan', 'ruam kulit'},
    'covid-19': {'demam', 'batuk', 'sesak napas', 'kehilangan indra penciuman', 'kelelahan'},
    'demam zika': {'demam', 'ruam kulit', 'nyeri sendi', 'nyeri otot', 'kelelahan'},
    'chikungunya': {'demam', 'nyeri sendi', 'ruam kulit', 'nyeri otot', 'kelelahan'},
    'leptospirosis': {'demam tinggi', 'nyeri otot', 'sakit kepala', 'mual', 'kulit kuning'},
    'ebola': {'demam tinggi', 'pendarahan', 'muntah', 'diare', 'nyeri otot'},
    'meningitis': {'demam tinggi', 'sakit kepala', 'leher kaku', 'mual', 'sensitivitas cahaya'},
    'encephalitis': {'demam', 'sakit kepala', 'kebingungan', 'kejang', 'kelelahan'},
    'rabies': {'demam', 'kesulitan menelan', 'kegelisahan', 'halusinasi', 'kelumpuhan'},
    'hepatitis b': {'kuning pada kulit dan mata', 'nyeri perut', 'kelelahan', 'mual', 'urin berwarna gelap'},
}

def forward_chaining(gejala):
    kemungkinan_penyakit = {}
    for penyakit, gejalanya in knowledge_base.items():
        cocok = gejalanya.intersection(gejala)
        kemungkinan_penyakit[penyakit] = len(cocok) / len(gejalanya)
    return kemungkinan_penyakit

def backward_chaining(penyakit, gejala):
    if penyakit in knowledge_base:
        return knowledge_base[penyakit].issubset(gejala)
    return False

def diagnose():
    user_input = entry.get()
    if not user_input:
        messagebox.showwarning("Input Error", "Masukkan gejala yang dialami.")
        return

    gejala = set(re.split(r',\s*', user_input.strip().lower()))


    diagnosis_forward = forward_chaining(gejala)


    result_text = "Kemungkinan penyakit dan persentase kecocokan:\n"
    for penyakit, persentase in sorted(diagnosis_forward.items(), key=lambda item: item[1], reverse=True):
        result_text += f"{penyakit}: {persentase * 100:.2f}%\n"


    confirmed_diseases = []
    for penyakit, persentase in diagnosis_forward.items():
        if persentase == 1.0:
            diagnosis_backward = backward_chaining(penyakit, gejala)
            if diagnosis_backward:
                confirmed_diseases.append(penyakit)
                result_text += f"Diagnosis (Backward Chaining) mengonfirmasi: {penyakit}\n"
            else:
                result_text += f"Diagnosis (Backward Chaining) tidak dapat mengkonfirmasi penyakit: {penyakit}\n"

    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, result_text)
    text_result.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Diagnosa Penyakit")
root.geometry("500x400")


label = tk.Label(root, text="Masukkan gejala yang dialami (pisahkan dengan koma):")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Diagnosa", command=diagnose)
button.pack(pady=10)

text_result = tk.Text(root, width=60, height=15, state=tk.DISABLED)
text_result.pack(pady=10)


root.mainloop()