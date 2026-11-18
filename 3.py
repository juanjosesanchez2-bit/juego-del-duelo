import streamlit as st

st.set_page_config(page_title="Desafío del Duelo", page_icon="💜", layout="centered")

QUESTIONS = [
("Comprender el duelo","¿Por qué ocurre el duelo en los seres humanos?",[
"Porque el cerebro humano olvida rápidamente las experiencias emocionales.",
"Porque el ser humano tiene una naturaleza social y afectiva.",
"Porque las personas adultas dejan de necesitar conexiones afectivas.",
"Porque todas las pérdidas producen la misma reacción."],1),
("Comprender el duelo","¿A qué se asocia normalmente el proceso de duelo, aunque su definición sea más amplia?",[
"A un cambio de residencia o mudanza.","A la pérdida de un objeto sin valor afectivo.",
"A la pérdida de un ser querido.","A cualquier cambio de rutina sin importancia emocional."],2),
("Duelo en la niñez","¿Por qué es fundamental acompañar a un niño en la elaboración de un duelo?",[
"Porque es un requisito social obligatorio.",
"Porque no elaborarlo puede afectar negativamente su psiquismo y bienestar emocional.",
"Porque los niños olvidan los sucesos tristes al instante.",
"Porque así se evita que vuelva a sentir tristeza."],1),
("Duelo en la niñez","¿Cómo suelen manifestar los niños pequeños el dolor de una pérdida?",[
"A través del juego, cambios de conducta o alteraciones en sus hábitos.",
"Escribiendo cuentos reflexivos.","Mediante un aislamiento social permanente.",
"Sin presentar ningún cambio en su comportamiento."],0),
("Duelo en la adolescencia","¿Por qué puede ser difícil afrontar un proceso de duelo durante la adolescencia?",[
"Porque los adolescentes no experimentan emociones fuertes.",
"Porque es una etapa de cambios emocionales, físicos y sociales.",
"Porque los adolescentes siempre superan rápidamente las pérdidas.",
"Porque no necesitan apoyo de otras personas."],1),
("Duelo en la adolescencia","¿Qué puede ayudar a un adolescente a afrontar un proceso de duelo?",[
"Evitar hablar sobre sus sentimientos.","Aislarse de sus familiares y amigos.",
"Expresar sus emociones y buscar apoyo en personas de confianza.","Ignorar lo sucedido."],2),
("Duelo en la adultez","¿Qué aspectos de la vida de un adulto pueden verse afectados durante un proceso de duelo?",[
"Únicamente su apariencia física.",
"Sus emociones, relaciones personales y responsabilidades laborales.",
"Solamente sus actividades recreativas.","Ningún aspecto de su vida cotidiana."],1),
("Duelo en la adultez","¿Por qué es importante el apoyo familiar y social durante el duelo en la adultez?",[
"Porque permite evitar por completo los sentimientos de tristeza.",
"Porque ayuda a olvidar rápidamente la pérdida.",
"Porque permite recibir comprensión, compañía y apoyo emocional.",
"Porque impide que la persona hable de lo sucedido."],2),
("Duelo en la vejez","¿Por qué el duelo puede ser especialmente significativo en la vejez?",[
"Porque las personas mayores suelen experimentar más pérdidas de seres queridos y cambios importantes en su vida.",
"Porque las personas mayores no establecen vínculos afectivos.",
"Porque el duelo desaparece con la edad.","Porque las personas mayores no necesitan acompañamiento."],0),
("Duelo en la vejez","¿Qué puede favorecer una mejor adaptación al duelo en la vejez?",[
"El acompañamiento emocional y el apoyo social.","El aislamiento permanente.",
"Evitar hablar de la pérdida.","Rechazar toda ayuda de personas cercanas."],0),
("Duelo y tecnología","¿Cómo puede ayudar la tecnología en los procesos de duelo?",[
"Facilita espacios de apoyo, comunicación y recuerdo de los seres queridos.",
"Elimina completamente el dolor de la pérdida.",
"Reemplaza la necesidad de apoyo emocional.",
"Hace que todas las personas vivan el duelo de la misma manera."],0),
("Duelo y tecnología","¿Qué son los griefbots mencionados en los estudios sobre duelo y tecnología?",[
"Sistemas tecnológicos que imitan conversaciones con personas fallecidas.",
"Medicamentos para tratar el duelo.","Programas para eliminar recuerdos dolorosos.",
"Aplicaciones que determinan cuánto debe durar un duelo."],0),
("Duelo y migración","¿Qué es el duelo migratorio?",[
"El proceso emocional relacionado con las pérdidas que experimenta una persona al dejar su país de origen.",
"El miedo a viajar en avión.","La pérdida de objetos durante un viaje.",
"La dificultad para organizar las maletas."],0),
("Duelo y migración","¿Qué pérdidas suelen estar asociadas al duelo migratorio?",[
"La separación de la familia, la cultura, el idioma y el entorno social.",
"Únicamente la pérdida económica.","Solo la pérdida de documentos personales.",
"La pérdida temporal de equipaje."],0),
]

LETTERS = ["A", "B", "C", "D"]
POINTS = 10
THRESHOLD = 65

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
html,body,[class*="css"]{font-family:Nunito,sans-serif}
.stApp{background:radial-gradient(circle at 5% 5%,#ffd9ec 0,transparent 27%),radial-gradient(circle at 95% 10%,#d9e4ff 0,transparent 28%),linear-gradient(135deg,#fff8fc,#f2f3ff 55%,#edfff9)}
.block-container{max-width:820px;padding-top:2rem}
.hero{background:linear-gradient(115deg,#7652d5,#b65bd2,#ef82b3);color:white;text-align:center;padding:28px;border-radius:25px;box-shadow:0 12px 28px #9275bd44;margin-bottom:18px}
.hero h1{color:white;font-weight:900;font-size:2.3rem;margin:0}
.hero p{color:#fff;font-size:1rem;margin-bottom:0}
.stat{background:#ffffffdf;border:1px solid #eee4ff;border-radius:16px;padding:12px;text-align:center}
.stat small{color:#817795;font-weight:900}.stat b{display:block;color:#704ac4;font-size:1.5rem}
.question{background:#fff;border:1px solid #eee5ff;border-radius:22px;padding:23px;margin:16px 0;box-shadow:0 9px 25px #6f5b9b18}
.tag{display:inline-block;background:#f0eaff;color:#704ac4;padding:6px 12px;border-radius:20px;font-weight:900;font-size:.85rem}
.qtext{font-size:1.3rem;font-weight:900;color:#30264b;margin-top:12px}
div.stButton>button{background:linear-gradient(90deg,#7652d5,#bb5bd0);color:white;border:0;border-radius:14px;font-weight:900;padding:.7rem}
div.stButton>button:hover{color:white;filter:brightness(1.08);transform:translateY(-1px)}
[data-testid="stRadio"] label{background:#fbfaff;border:1px solid #e9e1fa;border-radius:12px;padding:9px 12px}
</style>
""", unsafe_allow_html=True)

def restart():
    st.session_state.order=list(range(len(QUESTIONS)))
    st.session_state.pos=0
    st.session_state.score=0
    st.session_state.correct=0
    st.session_state.log=[]
    st.session_state.checked=False
    st.session_state.choice=None
    st.session_state.done=False

if "order" not in st.session_state:
    restart()

st.markdown('<div class="hero"><div style="font-size:2.2rem">💜 🌈 🦋</div><h1>EL DUELO Y LA MUERTE</h1><p>Un proceso del desarrollo humano</p></div>',unsafe_allow_html=True)

if not st.session_state.done:
    total=len(QUESTIONS); pos=st.session_state.pos
    a,b,c=st.columns(3)
    for col,label,value in [(a,"PREGUNTA",f"{pos+1}/{total}"),(b,"PUNTOS",st.session_state.score),(c,"ACIERTOS",st.session_state.correct)]:
        col.markdown(f'<div class="stat"><small>{label}</small><b>{value}</b></div>',unsafe_allow_html=True)
    st.progress(pos/total)
    cat,question,options,answer_idx=QUESTIONS[st.session_state.order[pos]]
    answer=options[answer_idx]
    st.markdown(f'<div class="question"><span class="tag">✨ {cat}</span><div class="qtext">{question}</div><p style="color:#817795">Selecciona una respuesta. Cada acierto suma {POINTS} puntos.</p></div>',unsafe_allow_html=True)

    choice=st.radio("Elige tu respuesta:",options,key=f"answer_{pos}",format_func=lambda x:f"{LETTERS[options.index(x)]}) {x}",index=None,disabled=st.session_state.checked)
    if not st.session_state.checked:
        if st.button("Comprobar respuesta 💫",use_container_width=True,disabled=choice is None):
            ok=choice==answer
            st.session_state.choice=choice
            st.session_state.checked=True
            if ok:
                st.session_state.score+=POINTS
                st.session_state.correct+=1
            st.session_state.log.append({"q":question,"chosen":choice,"answer":answer,"ok":ok})
            st.rerun()
    else:
        if st.session_state.choice==answer:
            st.success("¡Excelente! 🎉 Respuesta correcta. Sumaste 10 puntos.")
            st.balloons()
        else:
            st.error("¡Sigue aprendiendo! 💜 Esa no era la respuesta correcta.")
            st.info(f"Respuesta correcta: {answer}")
        if st.button("Siguiente pregunta ➜",use_container_width=True):
            st.session_state.pos+=1
            st.session_state.checked=False
            st.session_state.choice=None
            if st.session_state.pos>=total:
                st.session_state.done=True
            st.rerun()
    st.markdown("<p style='text-align:center;color:#9289aa;font-weight:800'>🌸 ¡Cada pregunta es una oportunidad para aprender! 🌸</p>",unsafe_allow_html=True)
else:
    total=len(QUESTIONS)
    pct=100*st.session_state.correct/total
    won=pct>THRESHOLD
    st.markdown('<div class="question" style="text-align:center">',unsafe_allow_html=True)
    if won:
        st.markdown("## 🏆 ¡FELICITACIONES, GANASTE!")
        st.success(f"Lograste {pct:.1f}% de respuestas correctas. ¡Superaste el 65%!")
        st.balloons()
    else:
        st.markdown("## 💜 ¡BUEN ESFUERZO!")
        st.info(f"Lograste {pct:.1f}%. Para ganar necesitas más del 65%. ¡Puedes volver a intentarlo!")
    x,y,z=st.columns(3)
    x.metric("Puntaje",f"{st.session_state.score}/{total*POINTS}")
    y.metric("Aciertos",f"{st.session_state.correct}/{total}")
    z.metric("Porcentaje",f"{pct:.1f}%")
    st.markdown('</div>',unsafe_allow_html=True)
    st.subheader("📚 Revisión de tus respuestas")
    for i,r in enumerate(st.session_state.log,1):
        with st.expander(f"{'✅' if r['ok'] else '❌'} Pregunta {i}: {r['q']}"):
            st.write("**Tu respuesta:**",r["chosen"])
            st.write("**Respuesta correcta:**",r["answer"])
    if st.button("🔄 Jugar de nuevo",use_container_width=True):
        restart()
        st.rerun()

st.markdown("---")
st.markdown("<p style='text-align:center;color:#9289aa'>Hecho para aprender con respeto y empatía 💜</p>",unsafe_allow_html=True)
