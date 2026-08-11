from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = "renacer2024"
WHATSAPP_URL = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"

def enviar_mensaje(numero_destino, texto):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": numero_destino,
        "type": "text",
        "text": {"body": texto}
    }
    response = requests.post(WHATSAPP_URL, headers=headers, json=data)
    print(f"📤 Mensaje enviado. Respuesta: {response.status_code}")
    return response.json()

def obtener_respuesta(mensaje):
    mensaje = mensaje.strip().lower()

    if mensaje in ["hola", "buenas", "buen dia", "buen día", "buenas tardes", "buenas noches", "hello", "hi", "menu", "menú", "inicio"]:
        return (
            "¡Hola! 👋 Bienvenida a *Estética Renacer* 🌸✨\n\n"
            "Nos alegra que nos escribas. ¿En qué podemos ayudarte hoy?\n\n"
            "1️⃣ Cómo agendar cita\n"
            "2️⃣ Ver nuestros tratamientos\n"
            "3️⃣ Formas de pago\n"
            "4️⃣ Síguenos en TikTok\n"
            "5️⃣ Hablar con una asesora\n\n"
            "Responde con el número de la opción. 💖"
        )

    elif mensaje == "1" or "cita" in mensaje or "agendar" in mensaje or "reservar" in mensaje or "horario" in mensaje:
        return (
            "📅 *Agenda tu cita en Renacer* ✨\n\n"
            "Atendemos *SOLO con cita previa* para brindarte una atención personalizada. 💖\n\n"
            "⚠️ Todos nuestros tratamientos son realizados *BAJO valoración previa*. 🩺\n\n"
            "Por favor envíanos:\n\n"
            "👤 Nombre completo\n"
            "💆 Tratamiento que deseas\n"
            "📆 Día que prefieres\n"
            "🕐 Hora aproximada\n\n"
            "Una vez confirmada tu cita, te enviaremos la ubicación exacta. 🌸"
        )

    elif mensaje == "2" or "servicio" in mensaje or "tratamiento" in mensaje:
        return (
            "✨ *Nuestros Tratamientos* 🌸\n\n"
            "Escribe el número del tratamiento que te interesa:\n\n"
            "🌟 *TRATAMIENTOS FACIALES*\n"
            "21 - Limpieza facial\n"
            "22 - Plasma rico en plaquetas (PRP)\n"
            "23 - Bioestimuladores\n"
            "24 - Exosomas\n"
            "25 - PDRN\n"
            "26 - Polinucleótidos\n"
            "27 - Rejuchip\n\n"
            "💉 *MEDICINA ESTÉTICA*\n"
            "28 - Toxina botulínica\n"
            "29 - Ácido hialurónico\n\n"
            "⚡ *TECNOLOGÍA AVANZADA*\n"
            "30 - Endoláser\n\n"
            "💃 *TRATAMIENTOS CORPORALES*\n"
            "31 - Tratamientos reductores\n"
            "32 - Levantamiento de glúteos\n"
            "33 - Tratamientos endovenosos\n\n"
            "⚠️ Todos se realizan *bajo valoración previa*. 🩺\n\n"
            "Escribe *menú* para volver al inicio. 💖"
        )

    elif mensaje == "3" or "pago" in mensaje or "yape" in mensaje:
        return (
            "💳 *Formas de pago en Renacer* ✨\n\n"
            "✅ Efectivo\n"
            "✅ Yape 📱\n"
            "✅ Transferencia bancaria\n\n"
            "Los detalles de pago se comparten al confirmar tu cita. 💖\n\n"
            "Escribe *menú* para volver al inicio."
        )

    elif mensaje == "4" or "tiktok" in mensaje or "redes" in mensaje:
        return (
            "🎥 *¡Síguenos en TikTok!* ✨\n\n"
            "Descubre nuestros tratamientos, resultados reales y tips de belleza. 🌸\n\n"
            "📱 *TikTok:* @Renacercentroestetico\n\n"
            "👉 https://www.tiktok.com/@renacercentroestetico\n\n"
            "¡No olvides seguirnos! 💖"
        )

    elif mensaje == "5" or "asesora" in mensaje or "precio" in mensaje or "cuanto" in mensaje or "cuánto" in mensaje:
        return (
            "🙋‍♀️ ¡Con gusto una asesora de *Renacer* te atenderá personalmente!\n\n"
            "En unos minutos te responderemos con toda la información. 💖\n\n"
            "Gracias por tu paciencia. 🌸"
        )

    elif mensaje == "21" or "limpieza facial" in mensaje:
        return ("✨ *Limpieza Facial* 🌸\n\nTratamiento que purifica y limpia tu piel a profundidad. Deja tu rostro fresco y renovado. 💖\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "22" or "plasma" in mensaje or "prp" in mensaje:
        return ("🩸 *Plasma Rico en Plaquetas (PRP)* ✨\n\nTratamiento regenerativo que rejuvenece la piel y estimula colágeno. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "23" or "bioestimulador" in mensaje:
        return ("🌟 *Bioestimuladores* ✨\n\nEstimulan la producción natural de colágeno para devolver firmeza y juventud a tu piel. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "24" or "exosomas" in mensaje:
        return ("🧬 *Exosomas* ✨\n\nTratamiento de última generación que regenera las células de la piel. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "25" or "pdrn" in mensaje:
        return ("💧 *PDRN* ✨\n\nTratamiento regenerativo que repara tejidos y mejora la elasticidad. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "26" or "polinucleotidos" in mensaje or "polinucleótidos" in mensaje:
        return ("🌸 *Polinucleótidos* ✨\n\nHidrata, rejuvenece y regenera la piel desde adentro. 💖\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "27" or "rejuchip" in mensaje:
        return ("✨ *Rejuchip* 🌸\n\nTratamiento innovador para rejuvenecimiento facial. 💖\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "28" or "botox" in mensaje or "botulinica" in mensaje or "botulínica" in mensaje:
        return ("💉 *Toxina Botulínica* ✨\n\nSuaviza arrugas y previene líneas de expresión. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "29" or "hialuronico" in mensaje or "hialurónico" in mensaje or "relleno" in mensaje:
        return ("💧 *Ácido Hialurónico* ✨\n\nRellenos para labios, ojeras, pómulos y mentón. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "30" or "endolaser" in mensaje or "endoláser" in mensaje:
        return ("⚡ *Endoláser* ✨\n\nTecnología láser para reducir grasa localizada y moldear tu figura. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "31" or "reductor" in mensaje or "adelgazar" in mensaje:
        return ("💃 *Tratamientos Reductores* ✨\n\nModela tu figura y reduce medidas de forma segura. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "32" or "gluteo" in mensaje or "glúteo" in mensaje:
        return ("🍑 *Levantamiento de Glúteos* ✨\n\nTonifica y da forma a tus glúteos sin cirugía. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif mensaje == "33" or "endovenoso" in mensaje or "vitamina" in mensaje or "suero" in mensaje:
        return ("💉 *Tratamientos Endovenosos* ✨\n\nVitaminas y nutrientes para revitalizar tu cuerpo. 🌸\n\n⚠️ Bajo valoración previa. 🩺\n\nEscribe *5* para más info o *2* para ver otros tratamientos.")

    elif "ubicacion" in mensaje or "ubicación" in mensaje or "direccion" in mensaje or "dirección" in mensaje or "donde" in mensaje or "dónde" in mensaje:
        return (
            "📍 *Sobre nuestra ubicación:*\n\n"
            "Por seguridad, la dirección se comparte *únicamente al confirmar tu cita*. 🔒💖\n\n"
            "Escribe *1* para agendar. 🌸\n\n"
            "🎥 Síguenos en TikTok: *@Renacercentroestetico*"
        )

    elif "gracias" in mensaje:
        return "¡Gracias a ti por confiar en *Renacer*! 🌸💖\n\nSíguenos en TikTok: *@Renacercentroestetico* ✨"

    elif "adios" in mensaje or "adiós" in mensaje or "chao" in mensaje or "bye" in mensaje:
        return "¡Hasta pronto! 💖 Te esperamos en *Estética Renacer* 🌸✨\n\n🎥 TikTok: *@Renacercentroestetico*"

    else:
        return (
            "No entendí tu mensaje 😅\n\n"
            "Por favor elige una opción:\n\n"
            "1️⃣ Cómo agendar cita\n"
            "2️⃣ Ver nuestros tratamientos\n"
            "3️⃣ Formas de pago\n"
            "4️⃣ Síguenos en TikTok\n"
            "5️⃣ Hablar con una asesora\n\n"
            "Escribe *menú* para volver al inicio. 💖"
        )

@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if mode == "subscribe" and token == "renacer2024":
        return challenge, 200
    return "Error de verificación", 403
    
@app.route("/webhook", methods=["POST"])
def recibir_mensaje():
    data = request.get_json()
    print(f"📥 Mensaje recibido: {data}")

    try:
        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        if "messages" in value:
            mensaje = value["messages"][0]
            numero_cliente = mensaje["from"]
            
            if mensaje["type"] == "text":
                texto = mensaje["text"]["body"]
                print(f"💬 De {numero_cliente}: {texto}")
                
                respuesta = obtener_respuesta(texto)
                enviar_mensaje(numero_cliente, respuesta)

    except Exception as e:
        print(f"⚠️ Error procesando mensaje: {e}")

    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def home():
    return "🌸 Bot de Estética Renacer funcionando ✨"

# Gunicorn se encarga de iniciar la app automáticamente en Render
