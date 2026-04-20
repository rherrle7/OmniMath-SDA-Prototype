import streamlit as st

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 'initial'

def set_stage(stage_name):
    st.session_state.stage = stage_name

def reset():
    st.session_state.stage = 'initial'

# --- UI Setup ---
st.set_page_config(page_title="OmniMath SDA", layout="centered")
st.markdown("## Socratic Distractor Analyzer")
st.markdown("### Solve: $x + 9 = 16$")
st.divider()

# --- State 1: Initial Problem ---
if st.session_state.stage == 'initial':
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("x = 7", on_click=set_stage, args=('correct',), use_container_width=True)
    with col2: st.button("x = 16", on_click=set_stage, args=('dist_16',), use_container_width=True)
    with col3: st.button("x = 25", on_click=set_stage, args=('dist_25',), use_container_width=True)
    with col4: st.button("x = 9", on_click=set_stage, args=('dist_9',), use_container_width=True)

# --- State 2: Correct Answer ---
elif st.session_state.stage == 'correct':
    st.success("Correct! $x = 7$")
    st.button("Try Another Problem", on_click=reset)

# ==========================================
# PATHWAY A: DISTRACTOR 25 (Added 9)
# ==========================================
elif st.session_state.stage == 'dist_25':
    st.warning("You selected **x = 25**. To arrive at 25, which of these best describes what you did?")
    st.button("I added 9 to both sides", on_click=set_stage, args=('mirror_25',))
    st.button("I subtracted 9 from both sides", on_click=set_stage, args=('trap_25',))
    st.button("I guessed", on_click=set_stage, args=('guessed',))

elif st.session_state.stage == 'trap_25':
    st.error("Wait a second. If you subtracted 9 from both sides, $16 - 9 = 7$. But you chose 25. Did you actually add 9, or did you guess?")
    st.button("I actually added 9", on_click=set_stage, args=('mirror_25',))
    st.button("I guessed", on_click=set_stage, args=('guessed',))

elif st.session_state.stage == 'mirror_25':
    st.info("Let's look at that: If we add 9 to both sides, we get $x + 9 + 9 = 16 + 9$, which simplifies to $x + 18 = 25$. Is $x$ by itself?")
    st.button("I see my mistake. Let me try again.", on_click=reset)
    st.button("I need help. Notify my teacher.", on_click=set_stage, args=('escalate',))


# ==========================================
# PATHWAY B: DISTRACTOR 16 (Balancing Error)
# ==========================================
elif st.session_state.stage == 'dist_16':
    st.warning("You selected **x = 16**. To arrive at 16, which of these best describes what you did?")
    st.button("I subtracted 9 from the left side only", on_click=set_stage, args=('mirror_16',))
    st.button("I subtracted 9 from the right side only", on_click=set_stage, args=('trap_16',))
    st.button("I guessed", on_click=set_stage, args=('guessed',))

elif st.session_state.stage == 'trap_16':
    st.error("Wait a second. If you subtracted 9 from the right side only, $16 - 9 = 7$. But you chose 16. Did you only subtract it from the left side, or did you guess?")
    st.button("I actually subtracted from the left only", on_click=set_stage, args=('mirror_16',))
    st.button("I guessed", on_click=set_stage, args=('guessed',))

elif st.session_state.stage == 'mirror_16':
    st.info("Let's look at that: If you only subtract 9 from the left, the equation becomes unbalanced, like a see-saw tipping over. Whatever we do to one side, we MUST do to the other to keep it equal.")
    st.button("I see my mistake. Let me try again.", on_click=reset)
    st.button("I need help. Notify my teacher.", on_click=set_stage, args=('escalate',))


# ==========================================
# PATHWAY C: DISTRACTOR 9 (Isolation Error)
# ==========================================
elif st.session_state.stage == 'dist_9':
    st.warning("You selected **x = 9**. To arrive at 9, which of these best describes what you did?")
    st.button("I removed the x instead of the 9", on_click=set_stage, args=('mirror_9',))
    st.button("I subtracted 7 from both sides", on_click=set_stage, args=('trap_9',))
    st.button("I guessed", on_click=set_stage, args=('guessed',))

elif st.session_state.stage == 'trap_9':
    st.error("Wait a second. If you subtracted 7 from both sides, $x + 2 = 9$. But you chose $x = 9$. Did you accidentally remove the x instead, or did you guess?")
    st.button("I actually removed the x", on_click=set_stage, args=('mirror_9',))
    st.button("I guessed", on_click=set_stage, args=('guessed',))

elif st.session_state.stage == 'mirror_9':
    st.info("Let's look at that: Our goal is to get $x$ completely by itself. If we remove $x$, we are left with $9 = 16$, which isn't mathematically true! We need to remove the number next to $x$, not $x$ itself.")
    st.button("I see my mistake. Let me try again.", on_click=reset)
    st.button("I need help. Notify my teacher.", on_click=set_stage, args=('escalate',))


# ==========================================
# GLOBAL STATES (Guessed / Escalated)
# ==========================================
elif st.session_state.stage == 'escalate':
    st.error("⚠️ **Concept Alert:** Please raise your hand and conference with your teacher.")
    # No reset button. The system locks until human intervention.

elif st.session_state.stage == 'guessed':
    st.info("Thanks for the honesty! Let's try again.")
    st.button("Reset", on_click=reset)
