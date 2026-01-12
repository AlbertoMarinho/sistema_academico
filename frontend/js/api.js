// API Helper Functions

const API = {
    // Alunos
    alunos: {
        getAll: async () => {
            const response = await fetch(`${API_BASE_URL}/alunos`);
            return response.json();
        },
        getById: async (id) => {
            const response = await fetch(`${API_BASE_URL}/alunos/${id}`);
            return response.json();
        },
        create: async (data) => {
            const response = await fetch(`${API_BASE_URL}/alunos`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        update: async (id, data) => {
            const response = await fetch(`${API_BASE_URL}/alunos/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        delete: async (id) => {
            const response = await fetch(`${API_BASE_URL}/alunos/${id}`, {
                method: 'DELETE'
            });
            return response.json();
        }
    },

    // Professores
    professores: {
        getAll: async () => {
            const response = await fetch(`${API_BASE_URL}/professores`);
            return response.json();
        },
        getById: async (id) => {
            const response = await fetch(`${API_BASE_URL}/professores/${id}`);
            return response.json();
        },
        create: async (data) => {
            const response = await fetch(`${API_BASE_URL}/professores`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        update: async (id, data) => {
            const response = await fetch(`${API_BASE_URL}/professores/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        delete: async (id) => {
            const response = await fetch(`${API_BASE_URL}/professores/${id}`, {
                method: 'DELETE'
            });
            return response.json();
        }
    },

    // Cursos
    cursos: {
        getAll: async () => {
            const response = await fetch(`${API_BASE_URL}/cursos`);
            return response.json();
        },
        getById: async (id) => {
            const response = await fetch(`${API_BASE_URL}/cursos/${id}`);
            return response.json();
        },
        create: async (data) => {
            const response = await fetch(`${API_BASE_URL}/cursos`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        update: async (id, data) => {
            const response = await fetch(`${API_BASE_URL}/cursos/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        delete: async (id) => {
            const response = await fetch(`${API_BASE_URL}/cursos/${id}`, {
                method: 'DELETE'
            });
            return response.json();
        }
    },

    // Disciplinas
    disciplinas: {
        getAll: async () => {
            const response = await fetch(`${API_BASE_URL}/disciplinas`);
            return response.json();
        },
        getByCurso: async (cursoId) => {
            const response = await fetch(`${API_BASE_URL}/disciplinas/curso/${cursoId}`);
            return response.json();
        },
        getById: async (id) => {
            const response = await fetch(`${API_BASE_URL}/disciplinas/${id}`);
            return response.json();
        },
        create: async (data) => {
            const response = await fetch(`${API_BASE_URL}/disciplinas`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        update: async (id, data) => {
            const response = await fetch(`${API_BASE_URL}/disciplinas/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        delete: async (id) => {
            const response = await fetch(`${API_BASE_URL}/disciplinas/${id}`, {
                method: 'DELETE'
            });
            return response.json();
        }
    },

    // Turmas
    turmas: {
        getAll: async () => {
            const response = await fetch(`${API_BASE_URL}/turmas`);
            return response.json();
        },
        getById: async (id) => {
            const response = await fetch(`${API_BASE_URL}/turmas/${id}`);
            return response.json();
        },
        getAlunos: async (id) => {
            const response = await fetch(`${API_BASE_URL}/turmas/${id}/alunos`);
            return response.json();
        },
        create: async (data) => {
            const response = await fetch(`${API_BASE_URL}/turmas`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        update: async (id, data) => {
            const response = await fetch(`${API_BASE_URL}/turmas/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        delete: async (id) => {
            const response = await fetch(`${API_BASE_URL}/turmas/${id}`, {
                method: 'DELETE'
            });
            return response.json();
        }
    },

    // Matrículas
    matriculas: {
        getAll: async () => {
            const response = await fetch(`${API_BASE_URL}/matriculas`);
            return response.json();
        },
        getByAluno: async (alunoId) => {
            const response = await fetch(`${API_BASE_URL}/matriculas/aluno/${alunoId}`);
            return response.json();
        },
        create: async (data) => {
            const response = await fetch(`${API_BASE_URL}/matriculas`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return response.json();
        },
        delete: async (id) => {
            const response = await fetch(`${API_BASE_URL}/matriculas/${id}`, {
                method: 'DELETE'
            });
            return response.json();
        }
    }
};