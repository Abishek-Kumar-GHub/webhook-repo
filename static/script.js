function formatEvent(event) {
    const date = new Date(event.timestamp);
    const timeStr = date.toUTCString();

    switch (event.action) {
        case "PUSH":
            return `${event.author} pushed to "${event.to_branch}" on ${timeStr}`;
        case "PULL REQUEST":
            return `${event.author} submitted a pull request from "${event.from_branch}" to "${event.to_branch}" on ${timeStr}`;
        case "MERGE":
            return `${event.author} merged branch "${event.from_branch}" to "${event.to_branch}" on ${timeStr}`;
        case "BRANCH CREATED":
            return `${event.author} created branch "${event.to_branch}" on ${timeStr}`;
        default:
            return `${event.author} performed "${event.action}" on ${timeStr}`;
    }
}

function fetchEvents() {
    fetch('/events')
        .then(response => response.json())
        .then(events => {
            const list = document.getElementById("events");
            list.innerHTML = "";
            events.forEach(event => {
                const item = document.createElement("li");
                item.textContent = formatEvent(event);
                list.appendChild(item);
            });
        });
}

setInterval(fetchEvents, 15000);
window.onload = fetchEvents;
