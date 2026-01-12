carregarTurmas();
carregarDisciplinasSelect();
carregarProfessoresSelect();

async function carregarDisciplinasSelect() {
    try {
        const response = await fetch(`${API_BASE_URL}/disciplinas`);
        const disciplinas = await response.json();
        const select = document.getElementById('disciplina_id');
        
        if (select) {
            disciplinas.forEach(disc => {
                const option = document.createElement('option');
                option.value = disc.id;
                option.textContent = disc.nome;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Erro:', error);
    }
}

async function carregarProfessoresSelect() {
    try {
        const response = await fetch(`${API_BASE_URL}/professores`);
        const professores = await response.json();
        const select = document.getElementById('professor_id');
        
        if (select) {
            professores.forEach(prof => {
                const option = document.createElement('option');
                option.value = prof.id;
                option.textContent = prof.nome;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Erro:', error);
    }
}

async function carregarTurmas() {
    const lista = document.getElementById('listaTurmas');
    if (!lista) return;
    
    showLoading(lista);
    
    try {
        const response = await fetch(`${API_BASE_URL}/turmas`);
        const turmas = await response.json();
        
        if (turmas.error) {
            lista.innerHTML = `<p style="color: red;">Erro: ${turmas.error}</p>`;
            return;
        }
        
        if (turmas.length === 0) {
            lista.innerHTML = '<p>Nenhuma turma cadastrada.</p>';
            return;
        }
        
        let html = `
            <table>
                <thead>
                    <tr>
                        <th>Código</th>
                        <th>Disciplina</th>
                        <th>Professor</th>
                        <th>Período</th>
                        <th>Ano</th>
                        <th>Vagas</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
        `;
        
        turmas.forEach(turma => {
            html += `
                <tr>
                    <td>${turma.codigo}</td>
                    <td>${turma.disciplina_nome || 'N/A'}</td>
                    <td>${turma.professor_nome || 'N/A'}</td>
                    <td>${turma.periodo}</td>
                    <td>${turma.ano}</td>
                    <td>${turma.vagas}</td>
                    <td>
                        <button class="btn-view" onclick="verAlunos(${turma.id})">Alunos</button>
                        <button class="btn-edit" onclick="editarTurma(${turma.id})">Editar</button>
                        <button class="btn-delete" onclick="excluirTurma(${turma.id}, '${turma.codigo.replace(/'/g, "\\'")}')">Excluir</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        lista.innerHTML = html;
    } catch (error) {
        console.error('Erro:', error);
        lista.innerHTML = '<p style="color: red;">Erro ao carregar turmas.</p>';
    }
}

async function salvarTurma(event) {
    event.preventDefault();
    
    const id = document.getElementById('turmaId').value;
    const data = {
        codigo: document.getElementById('codigo').value,
        disciplina_id: parseInt(document.getElementById('disciplina_id').value),
        professor_id: parseInt(document.getElementById('professor_id').value),
        periodo: document.getElementById('periodo').value,
        ano: parseInt(document.getElementById('ano').value),
        vagas: parseInt(document.getElementById('vagas').value)
    };
    
    try {
        let response;
        if (id) {
            response = await fetch(`${API_BASE_URL}/turmas/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        } else {
            response = await fetch(`${API_BASE_URL}/turmas`, {
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
        
        showAlert(id ? 'Turma atualizada!' : 'Turma cadastrada!');
        closeModal('modalTurma');
        document.getElementById('formTurma').reset();
        carregarTurmas();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao salvar turma', 'error');
    }
}

async function editarTurma(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/turmas/${id}`);
        const turma = await response.json();
        
        if (turma.error) {
            showAlert(turma.error, 'error');
            return;
        }
        
        document.getElementById('modalTitle').textContent = 'Editar Turma';
        document.getElementById('turmaId').value = turma.id;
        document.getElementById('codigo').value = turma.codigo;
        document.getElementById('disciplina_id').value = turma.disciplina_id;
        document.getElementById('professor_id').value = turma.professor_id;
        document.getElementById('periodo').value = turma.periodo;
        document.getElementById('ano').value = turma.ano;
        document.getElementById('vagas').value = turma.vagas;
        
        openModal('modalTurma');
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao carregar turma', 'error');
    }
}

async function excluirTurma(id, codigo) {
    if (!confirm(`Excluir turma ${codigo}?`)) return;
    
    try {
        const response = await fetch(`${API_BASE_URL}/turmas/${id}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        
        if (result.error) {
            showAlert(result.error, 'error');
            return;
        }
        
        showAlert('Turma excluída!');
        carregarTurmas();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao excluir turma', 'error');
    }
}

async function verAlunos(turmaId) {
    const lista = document.getElementById('listaAlunosTurma');
    if (!lista) return;
    
    showLoading(lista);
    
    try {
        const response = await fetch(`${API_BASE_URL}/turmas/${turmaId}/alunos`);
        const alunos = await response.json();
        
        if (alunos.length === 0) {
            lista.innerHTML = '<p>Nenhum aluno matriculado nesta turma.</p>';
        } else {
            let html = `
                <table>
                    <thead>
                        <tr>
                            <th>Nome</th>
                            <th>Email</th>
                            <th>Data Matrícula</th>
                        </tr>
                    </thead>
                    <tbody>
            `;
            
            alunos.forEach(aluno => {
                html += `
                    <tr>
                        <td>${aluno.aluno_nome}</td>
                        <td>${aluno.aluno_email}</td>
                        <td>${formatDate(aluno.data_matricula)}</td>
                    </tr>
                `;
            });
            
            html += '</tbody></table>';
            lista.innerHTML = html;
        }
        
        openModal('modalAlunos');
    } catch (error) {
        console.error('Erro:', error);
        lista.innerHTML = '<p style="color: red;">Erro ao carregar alunos.</p>';
    }
}

setTimeout(() => {
    const btnNovo = document.querySelector('.btn-primary');
    if (btnNovo) {
        const newBtn = btnNovo.cloneNode(true);
        btnNovo.parentNode.replaceChild(newBtn, btnNovo);
        newBtn.addEventListener('click', () => {
            document.getElementById('formTurma').reset();
            document.getElementById('turmaId').value = '';
            document.getElementById('modalTitle').textContent = 'Nova Turma';
        });
    }
}, 200);

console.log('✅ turmas.js carregado');