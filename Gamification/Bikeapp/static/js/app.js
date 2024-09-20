// Function to fetch challenges and display them
function loadChallenges() {
    fetch('/api/challenges/')
        .then(response => response.json())
        .then(data => {
            let challengeList = document.getElementById('challenge-list');
            data.forEach(challenge => {
                let challengeItem = document.createElement('div');
                challengeItem.innerHTML = `
                    <h3>${challenge.title}</h3>
                    <p>${challenge.description}</p>
                    <p>Points: ${challenge.points}</p>
                `;
                challengeList.appendChild(challengeItem);
            });
        });
}

// Function to fetch rewards and display them
function loadRewards() {
    fetch('/api/rewards/')
        .then(response => response.json())
        .then(data => {
            let rewardList = document.getElementById('reward-list');
            data.forEach(reward => {
                let rewardItem = document.createElement('div');
                rewardItem.innerHTML = `
                    <h3>${reward.name}</h3>
                    <p>${reward.description}</p>
                    <p>Points Required: ${reward.points_required}</p>
                `;
                rewardList.appendChild(rewardItem);
            });
        });
}

// Function to fetch user progress and display it
function loadUserProgress(username) {
    fetch(`/api/progress/${username}/`)  // Corrected template literal usage
        .then(response => response.json())
        .then(data => {
            let progressDiv = document.getElementById('user-progress');
            progressDiv.innerHTML = `
                <h3>User: ${data.user}</h3>
                <p>Points: ${data.points}</p>
                <p>Badges: ${data.badges}</p>
            `;
        });
}

// Call these functions based on the current page
if (window.location.pathname.includes('challenges')) {
    loadChallenges();
} else if (window.location.pathname.includes('rewards')) {
    loadRewards();
} else if (window.location.pathname.includes('progress')) {
    let username = "Likki"; // Replace with actual logged-in username
    loadUserProgress(username);
}
