export function obtainUserID() {
    let userId = localStorage.getItem('userId');
    if (!userId) {
        userId = Math.random().toString(36).substring(2, 12);
        localStorage.setItem('userId', userId);
    }
    return userId;
}