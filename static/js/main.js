const form = document.getElementById("planner-form");
const taskInput = document.getElementById("task");
const languageSelect = document.getElementById("language");
const modeSelect = document.getElementById("mode");

const loading = document.getElementById("loading");
const results = document.getElementById("results");
const summary = document.getElementById("summary");
const firstStep = document.getElementById("first-step");
const focusTip = document.getElementById("focus-tip");
const stepsList = document.getElementById("steps-list");

const contrastButton = document.getElementById("toggle-contrast");
const largeTextButton = document.getElementById("toggle-large-text");
const distractionsButton = document.getElementById("toggle-reduce-distractions");

const focusPanel = document.getElementById("focus-panel");
const enterFocusModeButton = document.getElementById("enter-focus-mode");
const nextStepButton = document.getElementById("next-step");
const exitFocusModeButton = document.getElementById("exit-focus-mode");
const focusStepCounter = document.getElementById("focus-step-counter");
const focusStepTitle = document.getElementById("focus-step-title");
const focusStepInstruction = document.getElementById("focus-step-instruction");

const timerPhase = document.getElementById("timer-phase");
const timerDisplay = document.getElementById("timer-display");
const timerStartButton = document.getElementById("timer-start");
const timerPauseButton = document.getElementById("timer-pause");
const timerResetButton = document.getElementById("timer-reset");
const timerApplyButton = document.getElementById("timer-apply");
const timerFeedback = document.getElementById("timer-feedback");
const timerStatusDot = document.getElementById("timer-status-dot");
const workMinutesInput = document.getElementById("work-minutes");
const breakMinutesInput = document.getElementById("break-minutes");

const historyList = document.getElementById("history-list");

let currentPlan = null;
let currentStepIndex = 0;

let timerInterval = null;
let timerSecondsRemaining = 15 * 60;
let timerMode = "work";
let timerIsRunning = false;
let timerWasPaused = false;

let customWorkMinutes = 15;
let customBreakMinutes = 5;

const uiTranslations = {
    en: {
        work: "Work",
        break: "Break",
        paused: "Paused",
        sessionComplete: "Session complete.",
        workStarted: "Work session started.",
        breakStarted: "Break started.",
        pausedMessage: "Timer paused.",
        reset: "Timer reset.",
        resume: "Resume",
        start: "Start",
        ready: "Plan ready.",
        customSaved: "Custom timer saved.",
        invalidTimer: "Please enter valid minute values.",
        step: "Step",
        historyEmpty: "No plans yet in this session.",
        planError: "The plan could not be generated right now.",
        submitting: "Building your plan...",
        emptyTask: "Write a task first.",
        focusOpened: "Focus mode ready.",
        focusClosed: "Focus mode closed.",
        finalStep: "You are already on the last step.",
        restoredState: "Your previous accessibility settings were restored."
    },
    es: {
        work: "Trabajo",
        break: "Pausa",
        paused: "Pausado",
        sessionComplete: "Sesión completada.",
        workStarted: "Sesión de trabajo iniciada.",
        breakStarted: "Pausa iniciada.",
        pausedMessage: "Temporizador pausado.",
        reset: "Temporizador reiniciado.",
        resume: "Reanudar",
        start: "Iniciar",
        ready: "Plan listo.",
        customSaved: "Temporizador personalizado guardado.",
        invalidTimer: "Ingresá valores válidos en minutos.",
        step: "Paso",
        historyEmpty: "Todavía no hay planes en esta sesión.",
        planError: "No se pudo generar el plan ahora mismo.",
        submitting: "Armando tu plan...",
        emptyTask: "Escribí primero una tarea.",
        focusOpened: "Modo foco listo.",
        focusClosed: "Modo foco cerrado.",
        finalStep: "Ya estás en el último paso.",
        restoredState: "Se restauraron tus preferencias de accesibilidad."
    }
};

const storageKeys = {
    history: "cognitive_helper_history",
    preferences: "cognitive_helper_preferences"
};

function getCurrentUiText() {
    return uiTranslations[languageSelect.value] || uiTranslations.en;
}

function showStatus(message, type = "neutral") {
    timerFeedback.textContent = message || "";

    timerFeedback.classList.remove(
        "status-neutral",
        "status-success",
        "status-warning",
        "status-error"
    );

    if (type === "success") {
        timerFeedback.classList.add("status-success");
    } else if (type === "warning") {
        timerFeedback.classList.add("status-warning");
    } else if (type === "error") {
        timerFeedback.classList.add("status-error");
    } else {
        timerFeedback.classList.add("status-neutral");
    }
}

function formatSeconds(totalSeconds) {
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}

function updateTimerDisplay() {
    timerDisplay.textContent = formatSeconds(timerSecondsRemaining);
}

function setTimerButtonsState() {
    const text = getCurrentUiText();

    timerStartButton.disabled = timerIsRunning;
    timerPauseButton.disabled = !timerIsRunning;
    timerApplyButton.disabled = timerIsRunning;

    timerStartButton.textContent = timerWasPaused ? text.resume : text.start;
}

function updateTimerPhaseLabel() {
    const text = getCurrentUiText();
    timerPhase.textContent = timerMode === "work" ? text.work : text.break;
}

function updateTimerVisualState() {
    timerStatusDot.classList.remove(
        "timer-status-work",
        "timer-status-break",
        "timer-status-paused"
    );

    if (timerIsRunning && timerMode === "work") {
        timerStatusDot.classList.add("timer-status-work");
    } else if (timerIsRunning && timerMode === "break") {
        timerStatusDot.classList.add("timer-status-break");
    } else {
        timerStatusDot.classList.add("timer-status-paused");
    }
}

function stopTimerInterval() {
    if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
}

function syncTimerInputsWithState() {
    workMinutesInput.value = customWorkMinutes;
    breakMinutesInput.value = customBreakMinutes;
}

function resetTimerState(showFeedback = true) {
    const text = getCurrentUiText();

    stopTimerInterval();
    timerIsRunning = false;
    timerWasPaused = false;
    timerMode = "work";
    timerSecondsRemaining = customWorkMinutes * 60;

    updateTimerPhaseLabel();
    updateTimerDisplay();
    updateTimerVisualState();
    setTimerButtonsState();

    if (showFeedback) {
        showStatus(text.reset, "neutral");
    } else {
        showStatus(text.ready, "neutral");
    }
}

function applyCustomTimer() {
    const text = getCurrentUiText();

    const nextWork = Number(workMinutesInput.value);
    const nextBreak = Number(breakMinutesInput.value);

    const workValid = Number.isInteger(nextWork) && nextWork >= 1 && nextWork <= 120;
    const breakValid = Number.isInteger(nextBreak) && nextBreak >= 1 && nextBreak <= 60;

    if (!workValid || !breakValid) {
        showStatus(text.invalidTimer, "error");
        return;
    }

    customWorkMinutes = nextWork;
    customBreakMinutes = nextBreak;

    timerMode = "work";
    timerSecondsRemaining = customWorkMinutes * 60;
    timerWasPaused = false;
    timerIsRunning = false;

    stopTimerInterval();
    updateTimerPhaseLabel();
    updateTimerDisplay();
    updateTimerVisualState();
    setTimerButtonsState();
    savePreferences();

    showStatus(text.customSaved, "success");
}

function startTimer() {
    const text = getCurrentUiText();

    if (timerIsRunning) return;

    timerIsRunning = true;

    if (timerMode === "work") {
        showStatus(text.workStarted, "success");
    } else {
        showStatus(text.breakStarted, "success");
    }

    stopTimerInterval();
    updateTimerVisualState();
    setTimerButtonsState();

    timerInterval = setInterval(() => {
        timerSecondsRemaining -= 1;
        updateTimerDisplay();

        if (timerSecondsRemaining <= 0) {
            handleTimerPhaseCompletion();
        }
    }, 1000);
}

function pauseTimer() {
    const text = getCurrentUiText();

    stopTimerInterval();
    timerIsRunning = false;
    timerWasPaused = true;

    updateTimerVisualState();
    setTimerButtonsState();

    showStatus(text.pausedMessage, "warning");
}

function handleTimerPhaseCompletion() {
    const text = getCurrentUiText();

    stopTimerInterval();
    timerIsRunning = false;
    timerWasPaused = false;

    if (timerMode === "work") {
        timerMode = "break";
        timerSecondsRemaining = customBreakMinutes * 60;
        showStatus(`${text.sessionComplete} ${text.breakStarted}`, "success");
    } else {
        timerMode = "work";
        timerSecondsRemaining = customWorkMinutes * 60;
        showStatus(`${text.sessionComplete} ${text.workStarted}`, "success");
    }

    updateTimerPhaseLabel();
    updateTimerDisplay();
    updateTimerVisualState();
    setTimerButtonsState();
    playCompletionSound();
}

function playCompletionSound() {
    try {
        const audioContext = new AudioContext();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);

        oscillator.type = "sine";
        oscillator.frequency.value = timerMode === "break" ? 880 : 660;
        gainNode.gain.value = 0.03;

        oscillator.start();
        oscillator.stop(audioContext.currentTime + 0.2);
    } catch (error) {
        // Ignore audio issues silently.
    }
}

function renderPlan(plan) {
    currentPlan = plan;
    currentStepIndex = 0;

    summary.textContent = plan.summary;
    firstStep.textContent = plan.first_step;
    focusTip.textContent = plan.focus_tip;

    stepsList.innerHTML = "";

    plan.steps.forEach((step) => {
        const li = document.createElement("li");

        const title = document.createElement("span");
        title.className = "step-title";
        title.textContent = step.title;

        const instruction = document.createElement("span");
        instruction.className = "step-instruction";
        instruction.textContent = step.instruction;

        const meta = document.createElement("div");
        meta.className = "step-meta";
        meta.textContent = `${step.minutes} min`;

        li.appendChild(title);
        li.appendChild(instruction);
        li.appendChild(meta);

        stepsList.appendChild(li);
    });

    results.classList.remove("d-none");
    renderFocusStep();
    renderHistoryEntry(plan);
}

function renderFocusStep() {
    if (!currentPlan || !currentPlan.steps.length) return;

    const text = getCurrentUiText();
    const step = currentPlan.steps[currentStepIndex];

    focusStepCounter.textContent = `${text.step} ${currentStepIndex + 1} / ${currentPlan.steps.length}`;
    focusStepTitle.textContent = step.title;
    focusStepInstruction.textContent = step.instruction;
}

function openFocusMode() {
    const text = getCurrentUiText();

    if (!currentPlan) return;

    focusPanel.classList.remove("d-none");
    renderFocusStep();
    resetTimerState(false);
    focusPanel.scrollIntoView({ behavior: "smooth", block: "start" });
    showStatus(text.focusOpened, "success");
}

function closeFocusMode() {
    const text = getCurrentUiText();

    focusPanel.classList.add("d-none");
    resetTimerState(false);
    showStatus(text.focusClosed, "neutral");
}

function goToNextStep() {
    const text = getCurrentUiText();

    if (!currentPlan) return;

    if (currentStepIndex < currentPlan.steps.length - 1) {
        currentStepIndex += 1;
        renderFocusStep();
        resetTimerState(false);
    } else {
        showStatus(text.finalStep, "warning");
    }
}

function getSessionHistory() {
    try {
        return JSON.parse(sessionStorage.getItem(storageKeys.history) || "[]");
    } catch (error) {
        return [];
    }
}

function saveSessionHistory(history) {
    sessionStorage.setItem(storageKeys.history, JSON.stringify(history));
}

function renderHistory() {
    const history = getSessionHistory();
    const text = getCurrentUiText();

    historyList.innerHTML = "";

    if (!history.length) {
        const empty = document.createElement("p");
        empty.className = "history-empty mb-0";
        empty.textContent = text.historyEmpty;
        historyList.appendChild(empty);
        return;
    }

    [...history].reverse().forEach((entry) => {
        const article = document.createElement("article");
        article.className = "history-item";

        const title = document.createElement("h4");
        title.className = "history-item-title";
        title.textContent = entry.task;

        const meta = document.createElement("p");
        meta.className = "history-item-meta";
        meta.textContent = `${entry.mode} • ${entry.language}`;

        const body = document.createElement("p");
        body.className = "history-item-body mb-0";
        body.textContent = entry.summary;

        article.appendChild(title);
        article.appendChild(meta);
        article.appendChild(body);

        historyList.appendChild(article);
    });
}

function renderHistoryEntry(plan) {
    const history = getSessionHistory();

    history.push({
        task: taskInput.value.trim(),
        language: languageSelect.value,
        mode: modeSelect.value,
        summary: plan.summary
    });

    saveSessionHistory(history);
    renderHistory();
}

function setPressedState(button, isPressed) {
    button.setAttribute("aria-pressed", String(isPressed));
}

function toggleBodyClass(button, className) {
    const isActive = document.body.classList.toggle(className);
    setPressedState(button, isActive);
    savePreferences();
}

function getPreferences() {
    try {
        return JSON.parse(localStorage.getItem(storageKeys.preferences) || "{}");
    } catch (error) {
        return {};
    }
}

function savePreferences() {
    const preferences = {
        highContrast: document.body.classList.contains("high-contrast"),
        largeText: document.body.classList.contains("large-text"),
        reduceDistractions: document.body.classList.contains("reduce-distractions"),
        workMinutes: customWorkMinutes,
        breakMinutes: customBreakMinutes
    };

    localStorage.setItem(storageKeys.preferences, JSON.stringify(preferences));
}

function applySavedPreferences() {
    const text = getCurrentUiText();
    const preferences = getPreferences();

    if (preferences.highContrast) {
        document.body.classList.add("high-contrast");
        setPressedState(contrastButton, true);
    }

    if (preferences.largeText) {
        document.body.classList.add("large-text");
        setPressedState(largeTextButton, true);
    }

    if (preferences.reduceDistractions) {
        document.body.classList.add("reduce-distractions");
        setPressedState(distractionsButton, true);
    }

    if (Number.isInteger(preferences.workMinutes) && preferences.workMinutes >= 1 && preferences.workMinutes <= 120) {
        customWorkMinutes = preferences.workMinutes;
    }

    if (Number.isInteger(preferences.breakMinutes) && preferences.breakMinutes >= 1 && preferences.breakMinutes <= 60) {
        customBreakMinutes = preferences.breakMinutes;
    }

    syncTimerInputsWithState();
    resetTimerState(false);

    if (
        preferences.highContrast ||
        preferences.largeText ||
        preferences.reduceDistractions ||
        preferences.workMinutes ||
        preferences.breakMinutes
    ) {
        showStatus(text.restoredState, "neutral");
    }
}

function clearPlanDisplay() {
    summary.textContent = "";
    firstStep.textContent = "";
    focusTip.textContent = "";
    stepsList.innerHTML = "";
}

async function submitPlan(event) {
    event.preventDefault();

    const text = getCurrentUiText();
    const task = taskInput.value.trim();
    const language = languageSelect.value;
    const mode = modeSelect.value;

    if (!task) {
        showStatus(text.emptyTask, "warning");
        taskInput.focus();
        return;
    }

    loading.classList.remove("d-none");
    results.classList.add("d-none");
    clearPlanDisplay();
    closeFocusMode();
    showStatus(text.submitting, "neutral");

    try {
        const response = await fetch("/api/plan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                task,
                language,
                mode
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || text.planError);
        }

        renderPlan(data.plan);
        results.scrollIntoView({ behavior: "smooth", block: "start" });
        showStatus(text.ready, "success");
    } catch (error) {
        console.error(error);
        showStatus(error.message || text.planError, "error");
    } finally {
        loading.classList.add("d-none");
    }
}

function syncLanguageInUrl() {
    const currentUrl = new URL(window.location.href);
    currentUrl.searchParams.set("lang", languageSelect.value);
    window.location.href = currentUrl.toString();
}

form.addEventListener("submit", submitPlan);
languageSelect.addEventListener("change", syncLanguageInUrl);

contrastButton.addEventListener("click", () => {
    toggleBodyClass(contrastButton, "high-contrast");
});

largeTextButton.addEventListener("click", () => {
    toggleBodyClass(largeTextButton, "large-text");
});

distractionsButton.addEventListener("click", () => {
    toggleBodyClass(distractionsButton, "reduce-distractions");
});

enterFocusModeButton.addEventListener("click", openFocusMode);
nextStepButton.addEventListener("click", goToNextStep);
exitFocusModeButton.addEventListener("click", closeFocusMode);

timerApplyButton.addEventListener("click", applyCustomTimer);
timerStartButton.addEventListener("click", startTimer);
timerPauseButton.addEventListener("click", pauseTimer);
timerResetButton.addEventListener("click", () => resetTimerState(true));

updateTimerPhaseLabel();
updateTimerDisplay();
updateTimerVisualState();
setTimerButtonsState();
syncTimerInputsWithState();
renderHistory();
applySavedPreferences();