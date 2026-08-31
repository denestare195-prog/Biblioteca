import streamlit as st
import streamlit.components.v1 as components

# =============================================================
# CONFIGURACIÓN GENERAL
# =============================================================
st.set_page_config(
    page_title="Biblioteca de Economía", page_icon="📚", layout="wide"
)

PORTADA_DEFECTO = "https://placehold.co/220x320/181818/e50914?text=Sin+Portada"


# =============================================================
# UTILIDADES
# =============================================================
def url_portada_drive(drive_id: str) -> str:
    return f"https://drive.google.com/thumbnail?id={drive_id}&sz=w400"


def url_descarga_drive(drive_id: str) -> str:
    return f"https://drive.google.com/uc?export=download&id={drive_id}"


def obtener_imagen_src(item: dict) -> str:
    if item.get("drive_id"):
        return url_portada_drive(item["drive_id"])
    return PORTADA_DEFECTO


# =============================================================
# DATOS: BIBLIOTECA
# Para agregar un libro nuevo, copia una entrada y cambia los
# valores. "id" debe ser único. "categoria" agrupa los libros
# en la interfaz (si la categoría no existe todavía, se crea
# sola al aparecer en la lista).
# =============================================================
LIBROS = [
    # --- Realidad Nacional ---
    {"id": 1, "titulo": "Brics", "autor": "Dr. C. Roberto Muñoz González & Dr. C. Bonifácio Vissetaca", "drive_id": "1rO9SnsctKcYeXg5mps5XM5x4fJU7wM1W", "categoria": "Realidad Nacional"},
    {"id": 2, "titulo": "Capitalismo actual", "autor": "Alejandro Dabat, Jorge Hernández & Canek Vega", "drive_id": "1YcngD-_DMw0qCyKqFjMlNUezoHa6bDPK", "categoria": "Realidad Nacional"},
    {"id": 3, "titulo": "Desigualdad", "autor": "Anastasio Ovejero", "drive_id": "18KcO5reez_VhgWcwRqxU-CwZ09HIS-sd", "categoria": "Realidad Nacional"},
    {"id": 4, "titulo": "El caso del Perú", "autor": "José Matos Mar", "drive_id": "1fKWKrK7Vc4J39qbzYLNHMw6uiKWMyoLU", "categoria": "Realidad Nacional"},
    {"id": 5, "titulo": "Estado Nación e Identidad Nacional", "autor": "Sonia García Segura", "drive_id": "11Vi0hbf7MggyvM9dX4tquhAK5M5fJ4Iv", "categoria": "Realidad Nacional"},
    {"id": 6, "titulo": "Historia e Identidad del Perú", "autor": "Oswaldo Holguín Callo", "drive_id": "1h0gKEvkmeYjkfPs47_46ysffhEXh4PEj", "categoria": "Realidad Nacional"},
    {"id": 7, "titulo": "La nueva corrupción en el Perú", "autor": "Óscar Ugarteche Galarza", "drive_id": "1kRBaRGFcB0UtFu3aRiVL9EOAJmLScidQ", "categoria": "Realidad Nacional"},
    {"id": 8, "titulo": "Nuevo orden", "autor": "Juan José Palacios L.", "drive_id": "1qlOkimhC8zLXCZdRmYoOx6cnM-Ilueom", "categoria": "Realidad Nacional"},
    {"id": 9, "titulo": "Oligarquía en el Perú", "autor": "Dennis Gilbert", "drive_id": "1CA8_C63lZRcP2HoGdQFyVg552vJ2RKO3", "categoria": "Realidad Nacional"},
    {"id": 10, "titulo": "Realidad Peruana", "autor": "Abelardo Hurtado, Wadson Pinchi & Norman Coronel", "drive_id": "1Buf7l02S0cdnp2I84FilcUz7U7uV7Zmt", "categoria": "Realidad Nacional"},
    {"id": 11, "titulo": "Sociedad de la información", "autor": "José Antonio Moreiro González", "drive_id": "10FRdSCjI42zGR6CyqTRtFLz-aM4fI_Ed", "categoria": "Realidad Nacional"},
    {"id": 12, "titulo": "Sociedad del conocimiento", "autor": "Adriana Marrero", "drive_id": "1vssz4OIiQS5o2H9Cb5haRxBjLiwmuFsZ", "categoria": "Realidad Nacional"},
    # --- Economía Política ---
    {"id": 13, "titulo": "El arte de la manipulación política", "autor": "Josep M. Colomer", "drive_id": "13PcyuJ5_dbwxhD0-FHtOTpf1PN8DNOrv", "categoria": "Economía Política"},
    {"id": 14, "titulo": "Democracia y participación", "autor": "Boaventura de Sousa Santos", "drive_id": "1KTSn63XwP7D3CoGDOCzLIC3vdgX6a6hC", "categoria": "Economía Política"},
    {"id": 15, "titulo": "Derecha e Izquierda: Razones y Significados de una Distinción", "autor": "Norberto Bobbio", "drive_id": "1k1eCfIu6a2Ar4v7OWYuKOFN6_oiadZvo", "categoria": "Economía Política"},
    {"id": 16, "titulo": "El Político y El Científico", "autor": "Max Weber", "drive_id": "1sCPyplbyr2Y_1DnKlwP-vkv18CUAK7v2", "categoria": "Economía Política"},
    {"id": 17, "titulo": "Ensayos de Mercadotecnia Política", "autor": "Pedro Barrientos Felipa", "drive_id": "1EBf8Iqtl8rnJyCwO2ORLASReAkEbJwbj", "categoria": "Economía Política"},
    {"id": 18, "titulo": "Gramsci", "autor": "Gramsci", "drive_id": "1oE82b6_vTquHjWQJIwd3m_7yHHKXDAxe", "categoria": "Economía Política"},
    {"id": 19, "titulo": "Historia y ciencias políticas", "autor": "Luis Alberto de la Garza", "drive_id": "10cA6A_ecG5IY2Oz8MGf_cFCVm4-pLW1w", "categoria": "Economía Política"},
    {"id": 20, "titulo": "La isla de los pingüinos", "autor": "Anatole France", "drive_id": "1M9ovCb1mOyv7QCb3V0X284t-mGU-9iQP", "categoria": "Economía Política"},
    {"id": 21, "titulo": "La política por dentro", "autor": "Rafael Roncagliolo & Carlos Meléndez", "drive_id": "134KIes4ZG1RhyAyEHcWCV1pWAcrdHOys", "categoria": "Economía Política"},
    {"id": 22, "titulo": "La Teoría de las Formas de Gobierno en la historia del pensamiento político", "autor": "Norberto Bobbio", "drive_id": "1qZtR1B0-q3HJvdVJfEQbXNj2B9O43IST", "categoria": "Economía Política"},
    {"id": 23, "titulo": "Manual de Campaña - Teoría y práctica de la persuasión electoral", "autor": "Mario Martínez Silva & Roberto Salcedo Aquino", "drive_id": "1z3PJhNd3MVyde85DGiJbFT2tt4ydWyFM", "categoria": "Economía Política"},
    {"id": 24, "titulo": "Manual de Ciencias Políticas", "autor": "Juan Manuel Abal Medina", "drive_id": "13Y_FCvhsuwhAqRc19Jk1rYAytZlpkofQ", "categoria": "Economía Política"},
    {"id": 25, "titulo": "Manual de Ciencia Política", "autor": "Miquel Caminal Badia", "drive_id": "1KaARp9Jns0Tc73HX0IV8kfte99XXDEAB", "categoria": "Economía Política"},
    {"id": 26, "titulo": "Manual de introducción a la ciencia política", "autor": "José Cazorla Pérez", "drive_id": "11fZJAjc26uUmIc7GKbLuoDhmTLvT4Lij", "categoria": "Economía Política"},
    {"id": 27, "titulo": "Política, Economía y Política Económica", "autor": "Leopoldo Fergusson", "drive_id": "19rndO0jN-Zzi-3qYKH2pUfuORHH9ZjlU", "categoria": "Economía Política"},
    {"id": 28, "titulo": "¿Qué es la democracia?", "autor": "Giovanni Sartori", "drive_id": "1QPBSE3d1wLVTIR8yjZ_Vsbr2PSf4GWPJ", "categoria": "Economía Política"},
    {"id": 29, "titulo": "Routledge Dictionary of Politics", "autor": "David Robertson", "drive_id": "1E8AYdQUq76DEIEjmCMAMAYDQjZJCc5WX", "categoria": "Economía Política"},
    # --- Estadística ---
    {"id": 30, "titulo": "Estadística aplicada a los negocios y la economía (3.ª ed.)", "autor": "Allen L. Webster", "drive_id": "1O_lMyCxWiXHCdzveMq-eoSiM-EtRANt6", "categoria": "Estadística"},
    {"id": 31, "titulo": "Procesamiento de datos y análisis utilizando SPSS", "autor": "Maria Belén Castañeda, Alberto F. Cabrera, Yadira Navarro & Wietse de Vries", "drive_id": "1Ymg-Y3naCRfMVohF567Vs6WDpVe_jV9U", "categoria": "Estadística"},
    {"id": 32, "titulo": "Probabilidad e inferencia estadística", "autor": "Rufino Moya C. & Gregorio Saravia A.", "drive_id": "1AJtZ6VkaxTo4d33ant3qkVls7rqYkI1m", "categoria": "Estadística"},
    {"id": 33, "titulo": "Estadística", "autor": "Mario F. Triola", "drive_id": "1o9B4sbe111_MwPyWz2QLWKPOPUSrekjL", "categoria": "Estadística"},
    {"id": 34, "titulo": "Estadística para administración", "autor": "Levin, Rubin, Banderas del Valle & Gómez", "drive_id": "171ysh9W0c9adGUITjLROjGmDMDKvN3v5", "categoria": "Estadística"},
    {"id": 35, "titulo": "Manual de estadística aplicada", "autor": "Jorge Córdova Egocheaga", "drive_id": "16sSIRNsS86JvrTld980BDN2oxmcFmOzo", "categoria": "Estadística"},
    {"id": 36, "titulo": "Estadística para ingenieros y científicos", "autor": "William Navidi", "drive_id": "1FwUOkxIHUMWMRTtuHBFyVCrd-SPb4G-1", "categoria": "Estadística"},
    {"id": 37, "titulo": "Un primer vistazo a la probabilidad", "autor": "Hildebrand", "drive_id": "1rHlfIJPxFYJqFzI1zC2Ix0OBwZXWr0cW", "categoria": "Estadística"},
    {"id": 38, "titulo": "Estadística descriptiva aplicada en Python", "autor": "Marcelo Bernavé Chancusig López, Guido Euclides Yauli Chicaiza, Guadalupe de las Mercedes López Castillo, José Antonio Andrade Valencia & Jhon Eduardo López Velasco", "drive_id": "1ulGQM7eJaWESgY3I2j_Xf2Yr6NOn0AnD", "categoria": "Estadística"},
    {"id": 39, "titulo": "Estadística para administración y economía", "autor": "Paul Newbold, William L. Carlson & Betty M. Thorne", "drive_id": "1Ju5g4NLSUBm300PNqXmTqf67gFXpULqc", "categoria": "Estadística"},
    {"id": 40, "titulo": "Estadística aplicada a los negocios y la economía", "autor": "Douglas A. Lind, William G. Marchal & Samuel A. Wathen", "drive_id": "1MrGYiXerNsOQzhl5hnBnv9Uc0W2IVxPf", "categoria": "Estadística"},
    {"id": 41, "titulo": "Estadística aplicada a administración y economía", "autor": "Leonard Kazmier & Alfredo Díaz Mata", "drive_id": "1YcGw3jK-vSqcg6Ksn5V4EF6ESJC8WOig", "categoria": "Estadística"},
    {"id": 42, "titulo": "Ciencia de datos", "autor": "Joel Grus", "drive_id": "1O7EbulQf4RzmzvIfcmdfq0nqbd9juHlc", "categoria": "Estadística"},
    {"id": 43, "titulo": "Estadística para administración y economía", "autor": "Anderson, Sweeney, Williams", "drive_id": "1gph4sFhogzhVPRfkz4E92cfye_yKFepe", "categoria": "Estadística"},
    # --- Microeconomía ---
    {"id": 44, "titulo": "Análisis microeconómico", "autor": "Hal R. Varian", "drive_id": "177QlcTiEKZmWh_lUWb04RsVsO5Rn0l7s", "categoria": "Microeconomía"},
    {"id": 45, "titulo": "Microeconomía intermedia (8.ª edición)", "autor": "Hal R. Varian", "drive_id": "1tVkDiHMDsgmxbXObY_KdTsAiZpsgD4qR", "categoria": "Microeconomía"},
    {"id": 46, "titulo": "Microeconomía intermedia: Un enfoque actual", "autor": "Hal R. Varian", "drive_id": "1LiB9vzwSNoGLpCRDNBkqxG_som1jg1gP", "categoria": "Microeconomía"},
    {"id": 47, "titulo": "Microeconomía (8.ª edición)", "autor": "Robert S. Pindyck & Daniel L. Rubinfeld", "drive_id": "1PIa-dPTi2hRMYGmMGrjxRKtrPmTUQp2C", "categoria": "Microeconomía"},
    {"id": 48, "titulo": "Microeconomía para productores", "autor": "Cecilia Garavito Masalías", "drive_id": "11ZwsCjMuvQQyZa3D8x0ykhnzNy1oO2Oc", "categoria": "Microeconomía"},
    {"id": 49, "titulo": "Microeconomía para Latinoamérica", "autor": "Michael Parkin", "drive_id": "12u8E94qey_ElXH7fLNB_WV6hJg-9YtYJ", "categoria": "Microeconomía"},
    {"id": 50, "titulo": "Microeconomía (7.ª edición)", "autor": "Robert S. Pindyck & Daniel L. Rubinfeld", "drive_id": "1PIa-dPTi2hRMYGmMGrjxRKtrPmTUQp2C", "categoria": "Microeconomía"},
    {"id": 51, "titulo": "Microeconomía", "autor": "Dominick Salvatore", "drive_id": "1lEDvBY--T0l-upKUZgdJEm91xY0lz-Sk", "categoria": "Microeconomía"},
    {"id": 52, "titulo": "Teoría microeconómica: Principios básicos y ampliaciones (9.ª ed.)", "autor": "Walter Nicholson", "drive_id": "1A8hQVqmRsLOo542ewYORZN7m60wJCv7S", "categoria": "Microeconomía"},
    {"id": 53, "titulo": "Teoría microeconómica (11.ª edición)", "autor": "Walter Nicholson & Christopher Snyder", "drive_id": "1B3x8Kfs02EwPqS0t8F7JbYGrwSFQVrZc", "categoria": "Microeconomía"},
    # --- Macroeconomía ---
    {"id": 54, "titulo": "Economía internacional: Teoría y política (10.ª edición)", "autor": "Paul R. Krugman, Maurice Obstfeld & Marc J. Melitz", "drive_id": "1siISkt_pnYsHxOZkBcKSNMrp6Y81EwP1", "categoria": "Macroeconomía"},
    {"id": 55, "titulo": "Keynes frente al viejo modelo clásico", "autor": "Anónimo", "drive_id": "18HoRHJIQxF--fYRdPLL0L-MDTh6FVzPC", "categoria": "Macroeconomía"},
    {"id": 56, "titulo": "Macroeconomía (10.ª edición)", "autor": "Rudiger Dornbusch, Stanley Fischer & Richard Startz", "drive_id": "1wAaXsCDJY90XczD3fsSE8utafYyFvd9w", "categoria": "Macroeconomía"},
    {"id": 57, "titulo": "Macroeconomía (7.ª edición)", "autor": "Olivier Blanchard", "drive_id": "176MzdZ-GzEE8hF9FPX-YiqQG2vyL43U2", "categoria": "Macroeconomía"},
    {"id": 58, "titulo": "Macroeconomía (8.ª edición)", "autor": "N. Gregory Mankiw", "drive_id": "1Bux3xsToCqYPSbhTrdViZ1tiPbQ8BIyH", "categoria": "Macroeconomía"},
    {"id": 59, "titulo": "Macroeconomía: Glosario básico", "autor": "Anónimo", "drive_id": "1Hk0w-hdj5Gf6QXiIuYarl-HfJ-9HIDxr", "categoria": "Macroeconomía"},
    {"id": 60, "titulo": "Modern Macroeconomics: Its Origins, Development and Current State", "autor": "Brian Snowdon & Howard R. Vane", "drive_id": "1QpGqoyErtlOdi9cq3R-Mky5vimMX-Qf7", "categoria": "Macroeconomía"},
    {"id": 61, "titulo": "Macroeconomía capital", "autor": "Miguel A. Alonso Neira", "drive_id": "18Oosaj9za277Laj8ZAJ8HfCnXX2ytsXd", "categoria": "Macroeconomía"},
    {"id": 62, "titulo": "Macroeconomía avanzada (3.ª edición)", "autor": "David Romer", "drive_id": "1MJY7EBXGJ2MXktxTC43MwsjrvzdeGfM7", "categoria": "Macroeconomía"},
    {"id": 63, "titulo": "Recursive Macroeconomic Theory (2nd edition)", "autor": "Lars Ljungqvist & Thomas J. Sargent", "drive_id": "11Bim3l34s3392FyN54omj5ZuMr8jAHbo", "categoria": "Macroeconomía"},
    {"id": 64, "titulo": "Tomo I: Macroeconomía - Modelos de Ciclos Económicos Reales", "autor": "Hamilton Galindo", "drive_id": "1P6Eok9xIBRU8cJWnQVjzzPS5T4d_WVtj", "categoria": "Macroeconomía"},
]

# =============================================================
# DATOS: RECURSOS DIDÁCTICOS
# Misma lógica que LIBROS: copia una entrada, cambia los datos.
# Reemplaza estos ejemplos por tus recursos reales.
# =============================================================
RECURSOS = [
    {"id": 1, "titulo": "Logo de economía", "autor": "", "drive_id": "1B4Vgzmfb0pJQUzLWessO9zv2_wfC1Vhu", "categoria": "General"},
]

# =============================================================
# DATOS: EXÁMENES
# Misma lógica que LIBROS y RECURSOS: copia una entrada, cambia
# los datos. "autor" puede usarse para el curso/ciclo/profesor.
# Reemplaza estos ejemplos por tus exámenes reales.
# =============================================================
EXAMENES = [
    {"id": 1, "titulo": "Examen parcial - Microeconomía", "autor": "Ciclo 2025-I", "drive_id": "", "categoria": "Microeconomía"},
    {"id": 2, "titulo": "Examen final - Estadística", "autor": "Ciclo 2025-I", "drive_id": "", "categoria": "Estadística"},
]


# =============================================================
# UTILIDADES DE RENDER (HTML)
# =============================================================
def escapar(texto: str) -> str:
    """Escapa comillas para insertar de forma segura dentro de atributos HTML."""
    return (texto or "").replace('"', "&quot;").replace("'", "&#39;")


# =============================================================
# ESTILOS DEL CARRUSEL (estilo Netflix, scroll horizontal por fila)
# =============================================================
CARRUSEL_CSS = """<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body {
    margin: 0; overflow-y: auto; overflow-x: hidden;
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #ffffff;
}
.fila-container { margin-bottom: 50px; animation: fadeInUp 0.6s ease-out; }
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.fila-titulo {
    font-size: 24px; font-weight: 800; color: #fff; margin: 0 0 20px 0;
    display: flex; align-items: center; gap: 10px; letter-spacing: 0.5px;
    text-transform: uppercase; position: relative; padding-left: 4px;
}
.fila-titulo::before {
    content: ''; width: 4px; height: 24px;
    background: linear-gradient(180deg, #e50914 0%, #ff1c1c 100%);
    border-radius: 2px;
}
.carousel-wrapper {
    position: relative; display: flex; align-items: center;
    gap: 12px; width: 100%; box-sizing: border-box;
}
.carousel-track {
    display: flex; flex: 1 1 0%; min-width: 0; gap: 16px;
    overflow-x: auto; overflow-y: hidden; scroll-behavior: smooth;
    padding: 10px 0 20px 0; scrollbar-width: none;
    -ms-overflow-style: none; scroll-snap-type: x mandatory; position: relative;
}
.carousel-track::-webkit-scrollbar { display: none; }
.carousel-track::before, .carousel-track::after {
    content: ''; position: absolute; top: 10px; height: calc(100% - 30px);
    width: 60px; pointer-events: none; opacity: 0; transition: opacity 0.3s; z-index: 2;
}
.carousel-track.show-left-fade::before {
    left: 0; opacity: 1;
    background: linear-gradient(90deg, rgba(15,15,15,0.8) 0%, transparent 100%);
}
.carousel-track.show-right-fade::after {
    right: 0; opacity: 1;
    background: linear-gradient(270deg, rgba(15,15,15,0.8) 0%, transparent 100%);
}
.netflix-card {
    flex: 0 0 180px; scroll-snap-align: start; border-radius: 12px;
    overflow: hidden; background: #1a1a1a; border: 1px solid #2d2d2d;
    transition: all 0.35s cubic-bezier(0.23, 1, 0.320, 1); cursor: pointer;
    display: flex; flex-direction: column; height: 320px; position: relative;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3); outline: none;
}
.netflix-card:focus, .netflix-card:focus-visible, .netflix-card:hover {
    transform: translateY(-12px) scale(1.05); border-color: #e50914; z-index: 20;
    box-shadow: 0 20px 50px rgba(229,9,20,0.4), 0 0 40px rgba(229,9,20,0.2);
}
.netflix-card:focus, .netflix-card:focus-visible { outline: 2px solid #e50914; outline-offset: 2px; }
.netflix-card::before {
    content: ''; position: absolute; inset: 0; opacity: 0; z-index: 1;
    background: linear-gradient(135deg, rgba(229,9,20,0.1) 0%, transparent 100%);
    transition: opacity 0.3s ease; pointer-events: none;
}
.netflix-card:hover::before { opacity: 1; }
.card-image {
    width: 100%; height: 220px; object-fit: cover; display: block;
    background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
    transition: transform 0.35s cubic-bezier(0.23, 1, 0.320, 1);
}
.netflix-card:hover .card-image { transform: scale(1.08); }
.card-info {
    padding: 12px; display: flex; flex-direction: column; flex-grow: 1;
    background: linear-gradient(180deg, #1a1a1a 0%, #0f0f0f 100%);
    justify-content: space-between; z-index: 2; gap: 6px;
}
.card-header { flex-grow: 1; }
.card-title {
    font-size: 13px; font-weight: 700; color: #fff; margin-bottom: 4px;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;
    overflow: hidden; line-height: 1.3; letter-spacing: 0.2px;
}
.card-author {
    font-size: 11px; color: #b0b0b0; display: -webkit-box;
    -webkit-line-clamp: 1; -webkit-box-orient: vertical; overflow: hidden; line-height: 1.2;
}
.download-btn {
    display: block; text-align: center; margin-top: auto; background: rgba(229, 9, 20, 0.9);
    color: #fff; font-size: 11px; font-weight: 700; text-decoration: none;
    padding: 7px 8px; border-radius: 6px; transition: background 0.2s, transform 0.2s;
}
.download-btn:hover { background: #e50914; transform: translateY(-1px); }
.download-btn.disabled { background: rgba(255,255,255,0.08); color: #888; cursor: not-allowed; pointer-events: none; }
.scroll-btn {
    background: rgba(30, 30, 30, 0.85); color: #fff; border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 24px; cursor: pointer; padding: 0; width: 44px; height: 72px; z-index: 15;
    border-radius: 8px; flex-shrink: 0; transition: all 0.2s cubic-bezier(0.23, 1, 0.320, 1);
    display: flex; align-items: center; justify-content: center; backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px); user-select: none; -webkit-user-select: none;
}
.scroll-btn:hover {
    background: rgba(229, 9, 20, 0.95); border-color: #e50914;
    transform: scale(1.08); box-shadow: 0 0 20px rgba(229, 9, 20, 0.5);
}
.scroll-btn:active { transform: scale(0.95); }
.scroll-btn.hidden { opacity: 0; pointer-events: none; }
.scroll-btn:focus-visible { outline: 2px solid #e50914; outline-offset: 2px; }
@media(max-width:1200px) { .netflix-card { flex: 0 0 160px; height: 300px; } .card-image { height: 200px; } .fila-titulo { font-size: 20px; } }
@media(max-width:768px) {
    .fila-container { margin-bottom: 40px; } .netflix-card { flex: 0 0 140px; height: 270px; }
    .card-image { height: 180px; } .card-info { padding: 10px; } .card-title { font-size: 12px; }
    .scroll-btn { width: 38px; height: 60px; font-size: 20px; } .carousel-wrapper { gap: 8px; }
    .carousel-track { gap: 12px; } .fila-titulo { font-size: 18px; }
}
@media(max-width:480px) {
    .netflix-card { flex: 0 0 120px; height: 240px; } .card-image { height: 160px; }
    .scroll-btn { width: 34px; height: 52px; } .carousel-track { gap: 10px; }
    .fila-titulo { font-size: 16px; } .card-title { font-size: 11px; }
    .card-author { font-size: 10px; } .download-btn { font-size: 10px; padding: 6px; }
}
</style>"""

CARRUSEL_JS = """<script>
function scrollCarousel(dir, trackId) {
    const track = document.getElementById(trackId);
    if (!track) return;
    const amount = track.clientWidth * 0.8;
    const mod = getComputedStyle(track).direction === 'rtl' ? -1 : 1;
    track.scrollBy({ left: dir === 'left' ? -amount * mod : amount * mod, behavior: 'smooth' });
    setTimeout(() => updateFadeIndicators(trackId), 300);
}

function updateFadeIndicators(trackId) {
    const track = document.getElementById(trackId);
    if (!track) return;
    const suf = trackId.replace('track_', '');
    const lBtn = document.getElementById(`scroll-left-${suf}`);
    const rBtn = document.getElementById(`scroll-right-${suf}`);
    const canL = track.scrollLeft > 10;
    const canR = track.scrollLeft < track.scrollWidth - track.clientWidth - 10;
    if (lBtn) lBtn.classList.toggle('hidden', !canL);
    if (rBtn) rBtn.classList.toggle('hidden', !canR);
    track.classList.toggle('show-left-fade', canL);
    track.classList.toggle('show-right-fade', canR);
}

function activarTarjeta(card) {
    if (!card) return;
    const btn = card.querySelector('a.download-btn');
    if (btn && !btn.classList.contains('disabled')) {
        window.open(btn.href, btn.target || '_blank');
    }
}

function initTracks() {
    document.querySelectorAll('.carousel-track').forEach(track => {
        track.addEventListener('scroll', () => updateFadeIndicators(track.id));
        updateFadeIndicators(track.id);
        track.addEventListener('wheel', (e) => {
            if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
            track.scrollLeft += e.deltaY;
            e.preventDefault();
        }, { passive: false });
        track.querySelectorAll('.netflix-card').forEach(card => {
            card.addEventListener('click', (e) => {
                if (!e.target.closest('a.download-btn')) activarTarjeta(card);
            });
        });
    });
}

document.addEventListener('keydown', (e) => {
    const active = document.activeElement?.closest?.('.netflix-card');
    if (!active) return;
    if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        const track = active.closest('.carousel-track');
        if (!track) return;
        const cards = Array.from(track.querySelectorAll('.netflix-card'));
        const idx = cards.indexOf(active);
        const nextIdx = e.key === 'ArrowRight'
            ? Math.min(idx + 1, cards.length - 1)
            : Math.max(idx - 1, 0);
        const next = cards[nextIdx];
        next.focus();
        next.scrollIntoView({ behavior: 'smooth', inline: 'nearest', block: 'nearest' });
        e.preventDefault();
    } else if (e.key === 'Enter' || e.key === ' ') {
        activarTarjeta(active);
        e.preventDefault();
    }
});

let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        document.querySelectorAll('.carousel-track').forEach(t => updateFadeIndicators(t.id));
    }, 250);
});

window.addEventListener('load', () => {
    document.querySelectorAll('.carousel-track').forEach(t => updateFadeIndicators(t.id));
});

initTracks();
</script>"""


# =============================================================
# ESTILOS GENERALES DE LA APP (fuera del carrusel)
# =============================================================
st.markdown(
    """
<style>
    #MainMenu, footer {visibility: hidden;}
    .stApp { background-color: #0e1117; }
</style>
""",
    unsafe_allow_html=True,
)


# =============================================================
# COMPONENTE: CARRUSEL DE ITEMS AGRUPADOS POR CATEGORÍA
# =============================================================
def mostrar_carrusel(items: list, buscador_key: str):
    if not items:
        st.info("Todavía no hay contenido en esta sección.")
        return

    busqueda = st.text_input(
        "🔍 Buscar por título o autor", key=buscador_key, placeholder="Escribe para filtrar..."
    ).strip().lower()

    items_filtrados = [
        i for i in items
        if busqueda in i["titulo"].lower() or busqueda in i["autor"].lower()
    ]

    if not items_filtrados:
        st.warning("No se encontraron resultados que coincidan con la búsqueda.")
        return

    # El orden de categorías sigue el orden en que aparecen los items en la lista.
    categorias_presentes = list(dict.fromkeys(i["categoria"] for i in items_filtrados))

    filas_html = ""
    for idx, categoria in enumerate(categorias_presentes):
        items_cat = [i for i in items_filtrados if i["categoria"] == categoria]
        track_id = f"track_{buscador_key}_{idx}"

        cards_html = ""
        for item in items_cat:
            img_src = obtener_imagen_src(item)
            titulo = escapar(item["titulo"])
            autor = escapar(item["autor"])
            drive_id = item.get("drive_id")

            if drive_id:
                boton = (
                    f'<a class="download-btn" href="{url_descarga_drive(drive_id)}" '
                    f'target="_blank" rel="noopener">📥 Descargar</a>'
                )
            else:
                boton = '<span class="download-btn disabled">No disponible</span>'

            cards_html += f"""
            <div class="netflix-card" tabindex="0">
                <img class="card-image" src="{img_src}" alt="{titulo}"
                     onerror="this.onerror=null;this.src='{PORTADA_DEFECTO}';">
                <div class="card-info">
                    <div class="card-header">
                        <div class="card-title" title="{titulo}">{titulo}</div>
                        <div class="card-author" title="{autor}">{('Autor: ' + autor) if autor else ''}</div>
                    </div>
                    {boton}
                </div>
            </div>
            """

        filas_html += f"""
        <div class="fila-container">
            <div class="fila-titulo">📌 {categoria}</div>
            <div class="carousel-wrapper">
                <button class="scroll-btn" id="scroll-left-{buscador_key}_{idx}" onclick="scrollCarousel('left', '{track_id}')">&#10094;</button>
                <div class="carousel-track" id="{track_id}">
                    {cards_html}
                </div>
                <button class="scroll-btn" id="scroll-right-{buscador_key}_{idx}" onclick="scrollCarousel('right', '{track_id}')">&#10095;</button>
            </div>
        </div>
        """

    html_completo = CARRUSEL_CSS + filas_html + CARRUSEL_JS
    # Altura estimada: título (~44px) + track con tarjetas de 320px
    # + padding vertical del track (~30px) + margen entre filas (50px) + margen extra.
    altura_estimada = 80 + len(categorias_presentes) * 450
    components.html(html_completo, height=altura_estimada, scrolling=False)


# =============================================================
# NAVEGACIÓN (barra lateral, se abre desde la izquierda)
# =============================================================
if "vista" not in st.session_state:
    st.session_state.vista = "Biblioteca"

SECCIONES = ["Biblioteca", "Recursos Didácticos", "Exámenes"]

with st.sidebar:
    st.title("📚 Menú")
    st.session_state.vista = st.radio(
        "Ir a:",
        SECCIONES,
        index=SECCIONES.index(st.session_state.vista)
        if st.session_state.vista in SECCIONES else 0,
        label_visibility="collapsed",
    )

# =============================================================
# CONTENIDO PRINCIPAL
# =============================================================
if st.session_state.vista == "Biblioteca":
    st.title("📚 Biblioteca de Economía")
    mostrar_carrusel(LIBROS, "buscar_libros")
elif st.session_state.vista == "Recursos Didácticos":
    st.title("🎓 Recursos Didácticos")
    mostrar_carrusel(RECURSOS, "buscar_recursos")
else:
    st.title("📝 Exámenes")
    mostrar_carrusel(EXAMENES, "buscar_examenes")
