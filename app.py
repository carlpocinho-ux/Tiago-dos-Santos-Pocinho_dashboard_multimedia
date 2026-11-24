import random
import unicodedata
from typing import Dict, List, Tuple

STOPWORDS = {
    "a", "o", "as", "os", "e", "é", "de", "da", "do", "das", "dos", "em", "na",
    "no", "nas", "nos", "um", "uma", "uns", "umas", "que", "se", "com", "por",
    "para", "pra", "ao", "aos", "à", "às", "ou", "mas", "como", "mais", "já",
    "não", "sim", "foi", "ser", "são", "era", "eu", "tu", "ele", "ela", "nós",
    "eles", "elas", "me", "te", "lhe", "meu", "teu", "seu", "nosso", "vamos",
    "algumas",
}

SINONIMOS: Dict[str, List[str]] = {
    "amor": ["afeto", "paixão", "ternura"],
    "luz": ["clarão", "brilho", "fulgor"],
    "mar": ["oceano", "vaga", "maresia"],
    "noite": ["escuridão", "breu", "penumbra"],
    "vida": ["existência", "jornada", "alento"],
    "tempo": ["instante", "era", "hora"],
    "sonho": ["devaneio", "fantasia", "utopia"],
    "coração": ["peito", "alma", "âmago"],
    "céu": ["firmamento", "abóbada", "azul"],
    "dor": ["mágoa", "angústia", "pena"],
    "alma": ["espírito", "essência", "íntimo"],
    "sol": ["astro-rei", "aurora", "dia"],
    "lua": ["luar", "astro", "selene"],
    "vento": ["brisa", "aragem", "sopro"],
    "saudade": ["nostalgia", "anseio", "falta"],
}

PALETAS: Dict[str, List[str]] = {
    "neon": ["#22d3ee", "#a78bfa", "#f472b6", "#fbbf24", "#34d399"],
    "viridis": ["#fde725", "#5ec962", "#21918c", "#3b528b", "#7e5aa8"],
    "plasma": ["#f0f921", "#f89540", "#cc4778", "#7e03a8", "#8b7cf6"],
    "fogo": ["#fff3b0", "#fbbf24", "#fb923c", "#ef4444", "#b91c1c"],
}


def analisar_texto(texto: str, max_palavras: int = 20, stopwords_extra: str = "") -> Dict:
    extra = {
        p.strip().lower()
        for p in stopwords_extra.replace(",", " ").split()
        if p.strip()
    }
    linhas = [linha for linha in texto.splitlines() if linha.strip()]
    palavras = [
        "".join(ch for ch in token.lower() if ch.isalpha() or ch == "-")
        for token in texto.split()
    ]
    palavras = [p for p in palavras if p]

    frequencias: Dict[str, int] = {}
    for p in palavras:
        if len(p) > 1 and p not in STOPWORDS and p not in extra:
            frequencias[p] = frequencias.get(p, 0) + 1

    top_palavras: List[Tuple[str, int]] = sorted(
        frequencias.items(), key=lambda item: item[1], reverse=True
    )[: max(1, max_palavras)]

    sugestoes = {
        palavra: SINONIMOS[palavra]
        for palavra, _ in top_palavras
        if palavra in SINONIMOS
    }

    return {
        "linhas": len(linhas),
        "total_palavras": len(palavras),
        "palavras_unicas": len(set(palavras)),
        "top_palavras": top_palavras,
        "sinonimos": sugestoes,
    }


PECAS_BATERIA = ["Bombo", "Tarola", "Hi-hat", "Tom 1", "Tom 2", "Timbalão", "Crash", "Ride"]

PADROES_PREDEFINIDOS: Dict[str, List[str]] = {
    "Rock": [
        "1000001010000000",
        "0000100000001000",
        "1010101010101010",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "1000000000000000",
        "0000000000000000",
    ],
    "Funk": [
        "1000001000110000",
        "0000100000001001",
        "1011101110111011",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
    ],
    "Disco": [
        "1000100010001000",
        "0000100000001000",
        "0010001000100010",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
    ],
    "Blast beat": [
        "1010101010101010",
        "0101010101010101",
        "1111111111111111",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "1000000000000000",
        "0000000000000000",
    ],
    "Rock com Ride": [
        "1000001010100000",
        "0000100000001000",
        "0000000000000000",
        "0000000000001000",
        "0000000000000100",
        "0000000000000011",
        "1000000000000000",
        "1010101010101010",
    ],
}


def criar_padrao(estilo: str) -> List[List[int]]:
    base = PADROES_PREDEFINIDOS.get(estilo, PADROES_PREDEFINIDOS["Rock"])
    return [[int(bit) for bit in linha] for linha in base]


def classificar_andamento(bpm: int) -> str:
    if bpm < 60:
        return "Largo (muito lento)"
    elif bpm < 76:
        return "Adagio (lento)"
    elif bpm < 108:
        return "Andante (moderado)"
    elif bpm < 120:
        return "Moderato"
    elif bpm < 168:
        return "Allegro (rápido)"
    else:
        return "Presto (muito rápido)"


def gerar_groove(estilo: str, dificuldade: int) -> List[List[int]]:
    padrao = criar_padrao(estilo)
    for _ in range(dificuldade * 2):
        linha = 0 if random.random() < 0.6 else 1
        passo = random.randrange(16)
        padrao[linha][passo] = 1
    if dificuldade == 3:
        toms_fill = [3, 3, 4, 5]
        for idx, passo in enumerate(range(12, 16)):
            padrao[toms_fill[idx]][passo] = 1 if random.random() < 0.75 else 0
    return padrao


def analisar_ritmo(padrao: List[List[int]], bpm: int) -> Dict:
    contagem_pecas = [sum(linha) for linha in padrao]
    total_notas = sum(contagem_pecas)
    densidade = round((total_notas / 128) * 100)
    sincopas = sum(
        1 for linha_idx in (0, 1) for passo, valor in enumerate(padrao[linha_idx]) if valor and passo % 4 != 0
    )
    if bpm > 160 or densidade > 50 or sincopas > 5:
        dificuldade_estimada = "Difícil"
    elif densidade > 30 or sincopas > 2:
        dificuldade_estimada = "Médio"
    else:
        dificuldade_estimada = "Fácil"

    return {
        "bpm": bpm,
        "andamento": classificar_andamento(bpm),
        "por_peca": dict(zip(PECAS_BATERIA, contagem_pecas)),
        "total_notas": total_notas,
        "densidade": densidade,
        "sincopas": sincopas,
        "dificuldade_estimada": dificuldade_estimada,
    }


PERGUNTAS = [
    (1, "Que modelo de cor usam os ecrãs? (sigla)", ["rgb"]),
    (1, "Que modelo de cor se usa na impressão? (sigla)", ["cmyk"]),
    (1, "Qual o formato de imagem vetorial da web? (sigla)", ["svg"]),
    (1, "Que linguagem estiliza as páginas web? (sigla)", ["css"]),
    (1, "Como se chama cada ponto de cor de um ecrã?", ["pixel"]),
    (2, "Quantas imagens por segundo (fps) tem o cinema tradicional?", ["24"]),
    (2, "Qual o formato de imagem comprimido mais usado em fotografias? (sigla)", ["jpg", "jpeg"]),
    (2, "Qual o formato de imagem sem perdas que suporta transparência? (sigla)", ["png"]),
    (2, "Qual o rácio de ecrã do Full HD?", ["16:9", "16/9"]),
    (2, "Qual o código hexadecimal do branco? (3 ou 6 dígitos)", ["ffffff", "fff"]),
    (3, "Quantos píxeis de largura tem o 4K UHD?", ["3840"]),
    (3, "Que codec de vídeo é o mais comum nos MP4? (H.264 ou AVC)", ["h.264", "h264", "avc"]),
    (3, "Que formato de áudio sem compressão é muito usado no Windows? (sigla)", ["wav"]),
    (3, "Qual o espaço de cor padrão da web? (sigla)", ["srgb"]),
    (3, "Qual a extensão dos ficheiros nativos do Photoshop?", ["psd"]),
    (1, "Qual a peça da bateria tocada com pedal que dá o som mais grave?", ["bombo", "bumbo"]),
    (1, "Como se chama o par de pratos que fecha com um pedal?", ["hi-hat", "hihat", "charleston", "charles", "chimbal"]),
    (2, "Quantos tempos tem cada compasso 4/4?", ["4", "quatro"]),
    (2, "Que unidade (sigla) mede o andamento de uma música?", ["bpm"]),
    (2, "Como se chama o tambor grande que fica no chão, ao lado da bateria?", ["timbalão", "tom de chão"]),
    (3, "Como se chama o andamento muito rápido, acima de 168 BPM?", ["presto"]),
    (3, "Como se chamam, em inglês, as notas muito suaves tocadas entre as principais na caixa?", ["ghost notes", "ghost note"]),
]

TEMPOS_POR_NIVEL = {1: 20, 2: 15, 3: 12, "m": 15}


def normalizar_resposta(texto: str) -> str:
    sem_acentos = "".join(
        ch for ch in unicodedata.normalize("NFD", texto.lower()) if unicodedata.category(ch) != "Mn"
    )
    return "".join(ch for ch in sem_acentos if ch not in {"#", " ", "\t", "\n"})


def gerar_dica_automatica(respostas_validas: List[str], tentativa: str = "") -> str:
    alvo = respostas_validas[0]
    tentativa_limpa = tentativa.strip()
    if alvo.isdigit() and tentativa_limpa.isdigit():
        relacao = "maior" if int(tentativa_limpa) > int(alvo) else "menor"
        return f"o teu número é {relacao} do que a resposta."
    if alvo.isdigit():
        return f"a resposta é um número com {len(alvo)} algarismos."
    return f'a resposta começa por "{alvo[0].upper()}" e tem {len(alvo)} caracteres.'


def verificar_resposta(respostas_validas: List[str], resposta_utilizador: str, tempo_esgotado: bool = False) -> bool:
    if tempo_esgotado:
        return False
    alvo_norm = normalizar_resposta(resposta_utilizador)
    return any(normalizar_resposta(valida) == alvo_norm for valida in respostas_validas)


if __name__ == "__main__":
    resumo = analisar_texto("O mar guarda a luz da noite\nLuz de mar", max_palavras=10)
    ritmo = analisar_ritmo(criar_padrao("Rock"), 100)
    print("Resumo texto:", resumo)
    print("Ritmo:", ritmo)