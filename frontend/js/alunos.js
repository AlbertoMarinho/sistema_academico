// Carregar alunos ao iniciar a página
carregarAlunos();

async function carregarAlunos() {
    const lista = document.getElementById('listaAlunos');
    if (!lista) {
        console.error('❌ Elemento #listaAlunos não encontrado');
        return;
    }
    
    showLoading(lista);
    
    try {
        const response = await fetch(`${API_BASE_URL}/alunos`);
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }
        
        const alunos = await response.json();
        console.log(`✅ ${alunos.length} alunos carregados`);
        
        if (alunos.error) {
            lista.innerHTML = `<p style="color: red;">Erro: ${alunos.error}</p>`;
            return;
        }
        
        if (alunos.length === 0) {
            lista.innerHTML = '<p>Nenhum aluno cadastrado. Clique em "+ Novo Aluno" para começar.</p>';
            return;
        }
        
        let html = `
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>CPF</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Data Nascimento</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
        `;
        
        alunos.forEach(aluno => {
            html += `
                <tr>
                    <td>${aluno.nome}</td>
                    <td>${aluno.cpf}</td>
                    <td>${aluno.email}</td>
                    <td>${aluno.telefone || '-'}</td>
                    <td>${formatDate(aluno.data_nascimento)}</td>
                    <td>
                        <button class="btn-edit" onclick="editarAluno(${aluno.id})">Editar</button>
                        <button class="btn-delete" onclick="excluirAluno(${aluno.id}, '${aluno.nome.replace(/'/g, "\\'")}')">Excluir</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        lista.innerHTML = html;
        
    } catch (error) {
        console.error('❌ Erro ao carregar alunos:', error);
        lista.innerHTML = `<p style="color: red;">Erro ao carregar alunos: ${error.message}</p>`;
    }
}

async function salvarAluno(event) {
    event.preventDefault();
    
    const id = document.getElementById('alunoId').value;
    const data = {
        nome: document.getElementById('nome').value,
        cpf: document.getElementById('cpf').value.replace(/\D/g, ''),
        email: document.getElementById('email').value,
        telefone: document.getElementById('telefone').value.replace(/\D/g, ''),
        data_nascimento: document.getElementById('data_nascimento').value
    };
    
    console.log('📤 Enviando dados:', data);
    
    try {
        let response;
        if (id) {
            response = await fetch(`${API_BASE_URL}/alunos/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        } else {
            response = await fetch(`${API_BASE_URL}/alunos`, {
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
        
        showAlert(id ? 'Aluno atualizado com sucesso!' : 'Aluno cadastrado com sucesso!');
        closeModal('modalAluno');
        document.getElementById('formAluno').reset();
        carregarAlunos();
        
    } catch (error) {
        console.error('❌ Erro ao salvar aluno:', error);
        showAlert('Erro ao salvar aluno: ' + error.message, 'error');
    }
}

async function editarAluno(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/alunos/${id}`);
        const aluno = await response.json();
        
        if (aluno.error) {
            showAlert(aluno.error, 'error');
            return;
        }
        
        document.getElementById('modalTitle').textContent = 'Editar Aluno';
        document.getElementById('alunoId').value = aluno.id;
        document.getElementById('nome').value = aluno.nome;
        document.getElementById('cpf').value = aluno.cpf;
        document.getElementById('email').value = aluno.email;
        document.getElementById('telefone').value = aluno.telefone || '';
        document.getElementById('data_nascimento').value = aluno.data_nascimento || '';
        
        openModal('modalAluno');
        
    } catch (error) {
        console.error('❌ Erro ao carregar aluno:', error);
        showAlert('Erro ao carregar dados do aluno', 'error');
    }
}

async function excluirAluno(id, nome) {
    if (!confirm(`Tem certeza que deseja excluir o aluno ${nome}?`)) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/alunos/${id}`, {
            method: 'DELETE'
        });
        
        const result = await response.json();
        
        if (result.error) {
            showAlert(result.error, 'error');
            return;
        }
        
        showAlert('Aluno excluído com sucesso!');
        carregarAlunos();
    } catch (error) {
        console.error('❌ Erro ao excluir aluno:', error);
        showAlert('Erro ao excluir aluno', 'error');
    }
}

// Configurar botão "Novo Aluno" - SEM usar const/let para evitar redeclaração
setTimeout(() => {
    const btnNovo = document.querySelector('.btn-primary');
    if (btnNovo) {
        // Remove listeners antigos
        const newBtn = btnNovo.cloneNode(true);
        btnNovo.parentNode.replaceChild(newBtn, btnNovo);
        
        newBtn.addEventListener('click', () => {
            document.getElementById('formAluno').reset();
            document.getElementById('alunoId').value = '';
            document.getElementById('modalTitle').textContent = 'Novo Aluno';
        });
        console.log('✅ Botão "Novo Aluno" configurado');
    }
}, 200);

console.log('✅ alunos.js carregado');