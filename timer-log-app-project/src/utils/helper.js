 function renderElapsedString(elapsed, runningSince) {
    let totalElapsed = elapsed;
    if (runningSince) {
        totalElapsed += Date.now() - runningSince;
    }
    return millisecondsToHuman(totalElapsed);
}

function millisecondsToHuman(ms) {
    const seconds = Math.floor((ms / 1000) % 60);
    const minutes = Math.floor((ms / 1000 / 60) % 60);
    const hours = Math.floor(ms / 1000 / 60 / 60);

    const humanized = [
        pad(hours.toString(), 2),
        pad(minutes.toString(), 2),
        pad(seconds.toString(), 2),
    ].join(':');

    return humanized;
}

function pad(numberString, size) {
    let papped = numberString;
    while (papped.length < size) papped = `0${papped}`;
    return papped;
}

function newTimer(attrs = {}) {
    const timer = {
        title: attrs.title || "Timer",
        project: attrs.project || "Project",
        id: Math.floor(Math.random() * 100),
        elapsed: 0,
    };
    return timer;
}

export { newTimer, renderElapsedString };