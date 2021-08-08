import axios from 'axios';

const BASE_URI = 'http://localhost:5000';

const client = axios.create({
 baseURL: BASE_URI,
 json: true
});

class APIClient {
    constructor() {
    }

    createKudo(repo) {
        return this.perform('post', '/kudos', repo);
    }

    deleteKudo(repo) {
        return this.perform('delete', `/kudos/${repo.id}`);
    }

    getKudos() {
        return this.perform('get', '/kudos');
    }

    backend() {
        return this.perform('get', '/backend');
    }

    async perform (method, resource, data) {
        return client({
            method,
            url: resource,
            data,
	        /*
            headers: {
                Authorization: `Bearer ${this.accessToken}`
            }
            */
        }).then(resp => {
            return resp.data ? resp.data : [];
        })
    }
}

export default APIClient;
