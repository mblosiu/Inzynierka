import axios from 'axios';

export default () => {
    //let currentUser = JSON.parse(window.localStorage.currentUser);
    return axios.create({
        baseURL: 'http://127.0.0.1:8000/api',
        withCredentials: false,
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            //Authorization: currentUser //&& currentUser.token
        }
    });
}