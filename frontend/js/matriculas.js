carregarMatriculas();
carregarAlunosSelect();
carregarTurmasSelect();

async function carregarAlunosSelect() {
    try {
        const response = await fetch(`${API_BASE_URL}/alunos`);
        const alunos = await response.json();
        const select = document.getElementById('aluno_id');
        
        if (select) {
            alunos.forEach(aluno => {
                const option = document.createElement('option');
                option.value = aluno.id;
                option.textContent = aluno.nome;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Erro:', error);
    }
}

async function carregarTurmasSelect() {
    try {
        const response = await fetch(`${API_BASE_URL}/turmas`);
        const turmas = await response.json();
        const select = document.getElementById('turma_id');
        
        if (select) {
            turmas.forEach(turma => {
                const option = document.createElement('option');
                option.value = turma.id;
                option.textContent = `${turma.codigo} - ${turma.disciplina_nome || 'N/A'}`;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Erro:', error);
    }
}

async function carregarMatriculas() {
    const lista = document.getElementById('listaMatriculas');
    if (!lista) return;
    
    showLoading(lista);
    
    try {
        const response = await fetch(`${API_BASE_URL}/matriculas`);
        const matriculas = await response.json();
        
        if (matriculas.error) {
            lista.innerHTML = `<p style="color: red;">Erro: ${matriculas.error}</p>`;
            return;
        }
        
        if (matriculas.length === 0) {
            lista.innerHTML = '<p>Nenhuma matrícula cadastrada.</p>';
            return;
        }
        
        let html = `
            <table>
                <thead>
                    <tr>
                        <th>Aluno</th>
                        <th>Turma</th>
                        <th>Data Matrícula</th>
                        <th>Status</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
        `;
        
        matriculas.forEach(mat => {
            html += `
                <tr>
                    <td>${mat.aluno_nome || 'N/A'}</td>
                    <td>${mat.turma_codigo || 'N/A'}</td>
                    <td>${formatDate(mat.data_matricula)}</td>
                    <td>${mat.status}</td>
                    <td>
                        <button class="btn-delete" onclick="cancelarMatricula(${mat.id}, '${(mat.aluno_nome || '').replace(/'/g, "\\'")}')">Cancelar</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        lista.innerHTML = html;
    } catch (error) {
        console.error('Erro:', error);
        lista.innerHTML = '<p style="color: red;">Erro ao carregar matrículas.</p>';
    }
}

async function salvarMatricula(event) {
    event.preventDefault();
    
    const data = {
        aluno_id: parseInt(document.getElementById('aluno_id').value),
        turma_id: parseInt(document.getElementById('turma_id').value)
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/matriculas`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        if (result.error) {
            showAlert(result.error, 'error');
            return;
        }
        
        showAlert('Matrícula realizada com sucesso!');
        closeModal('modalMatricula');
        document.getElementById('formMatricula').reset();
        carregarMatriculas();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao realizar matrícula', 'error');
    }
}

async function cancelarMatricula(id, aluno) {
    if (!confirm(`Cancelar matrícula de ${aluno}?`)) return;
    
    try {
        const response = await fetch(`${API_BASE_URL}/matriculas/${id}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        
        if (result.error) {
            showAlert(result.error, 'error');
            return;
        }
        
        showAlert('Matrícula cancelada!');
        carregarMatriculas();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao cancelar matrícula', 'error');
    }
}

setTimeout(() => {
    const btnNovo = document.querySelector('.btn-primary');
    if (btnNovo) {
        const newBtn = btnNovo.cloneNode(true);
        btnNovo.parentNode.replaceChild(newBtn, btnNovo);
        newBtn.addEventListener('click', () => {
            document.getElementById('formMatricula').reset();
        });
    }
}, 200);

console.log('✅ matriculas.js carregado');