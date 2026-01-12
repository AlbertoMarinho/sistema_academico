carregarDisciplinas();
carregarCursosSelect();

async function carregarCursosSelect() {
    try {
        const response = await fetch(`${API_BASE_URL}/cursos`);
        const cursos = await response.json();
        const select = document.getElementById('curso_id');
        
        if (select) {
            cursos.forEach(curso => {
                const option = document.createElement('option');
                option.value = curso.id;
                option.textContent = curso.nome;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Erro ao carregar cursos:', error);
    }
}

async function carregarDisciplinas() {
    const lista = document.getElementById('listaDisciplinas');
    if (!lista) return;
    
    showLoading(lista);
    
    try {
        const response = await fetch(`${API_BASE_URL}/disciplinas`);
        const disciplinas = await response.json();
        const responseCursos = await fetch(`${API_BASE_URL}/cursos`);
        const cursos = await responseCursos.json();
        
        if (disciplinas.error) {
            lista.innerHTML = `<p style="color: red;">Erro: ${disciplinas.error}</p>`;
            return;
        }
        
        if (disciplinas.length === 0) {
            lista.innerHTML = '<p>Nenhuma disciplina cadastrada.</p>';
            return;
        }
        
        let html = `
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Código</th>
                        <th>Carga Horária</th>
                        <th>Curso</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
        `;
        
        disciplinas.forEach(disc => {
            const curso = cursos.find(c => c.id === disc.curso_id);
            const nomeCurso = curso ? curso.nome : 'N/A';
            
            html += `
                <tr>
                    <td>${disc.nome}</td>
                    <td>${disc.codigo}</td>
                    <td>${disc.carga_horaria}h</td>
                    <td>${nomeCurso}</td>
                    <td>
                        <button class="btn-edit" onclick="editarDisciplina(${disc.id})">Editar</button>
                        <button class="btn-delete" onclick="excluirDisciplina(${disc.id}, '${disc.nome.replace(/'/g, "\\'")}')">Excluir</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        lista.innerHTML = html;
    } catch (error) {
        console.error('Erro:', error);
        lista.innerHTML = '<p style="color: red;">Erro ao carregar disciplinas.</p>';
    }
}

async function salvarDisciplina(event) {
    event.preventDefault();
    
    const id = document.getElementById('disciplinaId').value;
    const data = {
        nome: document.getElementById('nome').value,
        codigo: document.getElementById('codigo').value,
        carga_horaria: parseInt(document.getElementById('carga_horaria').value),
        curso_id: parseInt(document.getElementById('curso_id').value)
    };
    
    try {
        let response;
        if (id) {
            response = await fetch(`${API_BASE_URL}/disciplinas/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        } else {
            response = await fetch(`${API_BASE_URL}/disciplinas`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        }
        
        const result = await response.json();
        if (result.error) {
            showAlert(result.error, 'error');
            return;
        }
        
        showAlert(id ? 'Disciplina atualizada!' : 'Disciplina cadastrada!');
        closeModal('modalDisciplina');
        document.getElementById('formDisciplina').reset();
        carregarDisciplinas();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao salvar disciplina', 'error');
    }
}

async function editarDisciplina(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/disciplinas/${id}`);
        const disc = await response.json();
        
        if (disc.error) {
            showAlert(disc.error, 'error');
            return;
        }
        
        document.getElementById('modalTitle').textContent = 'Editar Disciplina';
        document.getElementById('disciplinaId').value = disc.id;
        document.getElementById('nome').value = disc.nome;
        document.getElementById('codigo').value = disc.codigo;
        document.getElementById('carga_horaria').value = disc.carga_horaria;
        document.getElementById('curso_id').value = disc.curso_id;
        
        openModal('modalDisciplina');
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao carregar disciplina', 'error');
    }
}

async function excluirDisciplina(id, nome) {
    if (!confirm(`Excluir disciplina ${nome}?`)) return;
    
    try {
        const response = await fetch(`${API_BASE_URL}/disciplinas/${id}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        
        if (result.error) {
            showAlert(result.error, 'error');
            return;
        }
        
        showAlert('Disciplina excluída!');
        carregarDisciplinas();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao excluir disciplina', 'error');
    }
}

setTimeout(() => {
    const btnNovo = document.querySelector('.btn-primary');
    if (btnNovo) {
        const newBtn = btnNovo.cloneNode(true);
        btnNovo.parentNode.replaceChild(newBtn, btnNovo);
        newBtn.addEventListener('click', () => {
            document.getElementById('formDisciplina').reset();
            document.getElementById('disciplinaId').value = '';
            document.getElementById('modalTitle').textContent = 'Nova Disciplina';
        });
    }
}, 200);

console.log('✅ disciplinas.js carregado');