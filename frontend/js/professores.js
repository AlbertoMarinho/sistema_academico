carregarProfessores();

async function carregarProfessores() {
    const lista = document.getElementById('listaProfessores');
    if (!lista) return;
    
    showLoading(lista);
    
    try {
        const response = await fetch(`${API_BASE_URL}/professores`);
        const professores = await response.json();
        
        if (professores.error) {
            lista.innerHTML = `<p style="color: red;">Erro: ${professores.error}</p>`;
            return;
        }
        
        if (professores.length === 0) {
            lista.innerHTML = '<p>Nenhum professor cadastrado.</p>';
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
                        <th>Especialização</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
        `;
        
        professores.forEach(prof => {
            html += `
                <tr>
                    <td>${prof.nome}</td>
                    <td>${prof.cpf}</td>
                    <td>${prof.email}</td>
                    <td>${prof.telefone || '-'}</td>
                    <td>${prof.especializacao || '-'}</td>
                    <td>
                        <button class="btn-edit" onclick="editarProfessor(${prof.id})">Editar</button>
                        <button class="btn-delete" onclick="excluirProfessor(${prof.id}, '${prof.nome.replace(/'/g, "\\'")}')">Excluir</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        lista.innerHTML = html;
        
    } catch (error) {
        console.error('Erro:', error);
        lista.innerHTML = '<p style="color: red;">Erro ao carregar professores.</p>';
    }
}

async function salvarProfessor(event) {
    event.preventDefault();
    
    const id = document.getElementById('professorId').value;
    const data = {
        nome: document.getElementById('nome').value,
        cpf: document.getElementById('cpf').value.replace(/\D/g, ''),
        email: document.getElementById('email').value,
        telefone: document.getElementById('telefone').value.replace(/\D/g, ''),
        especializacao: document.getElementById('especializacao').value
    };
    
    try {
        let response;
        if (id) {
            response = await fetch(`${API_BASE_URL}/professores/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        } else {
            response = await fetch(`${API_BASE_URL}/professores`, {
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
        
        showAlert(id ? 'Professor atualizado!' : 'Professor cadastrado!');
        closeModal('modalProfessor');
        document.getElementById('formProfessor').reset();
        carregarProfessores();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao salvar professor', 'error');
    }
}

async function editarProfessor(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/professores/${id}`);
        const prof = await response.json();
        
        if (prof.error) {
            showAlert(prof.error, 'error');
            return;
        }
        
        document.getElementById('modalTitle').textContent = 'Editar Professor';
        document.getElementById('professorId').value = prof.id;
        document.getElementById('nome').value = prof.nome;
        document.getElementById('cpf').value = prof.cpf;
        document.getElementById('email').value = prof.email;
        document.getElementById('telefone').value = prof.telefone || '';
        document.getElementById('especializacao').value = prof.especializacao || '';
        
        openModal('modalProfessor');
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao carregar professor', 'error');
    }
}

async function excluirProfessor(id, nome) {
    const result = await Swal.fire({
        title: 'Tem certeza?',
        text: `Deseja excluir o professor ${nome}?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Cancelar'
    });

    if (!result.isConfirmed) return;

    try {
        const response = await fetch(`${API_BASE_URL}/professores/${id}`, {
            method: 'DELETE'
        });
        const result = await response.json();

        if (result.error) {
            Swal.fire('Erro!', result.error, 'error');
            return;
        }

        Swal.fire('Excluído!', 'Professor removido com sucesso.', 'success');
        carregarProfessores();
    } catch (error) {
        console.error('Erro:', error);
        Swal.fire('Erro!', 'Falha ao conectar com o servidor.', 'error');
    }
}

// Configurar botão e máscaras
setTimeout(() => {
    // Aplica a máscara de telefone (definida no app.js)
    aplicarMascaras();

    const btnNovo = document.querySelector('.btn-primary');
    if (btnNovo) {
        const newBtn = btnNovo.cloneNode(true);
        btnNovo.parentNode.replaceChild(newBtn, btnNovo);
        newBtn.addEventListener('click', () => {
            document.getElementById('formProfessor').reset();
            document.getElementById('professorId').value = '';
            document.getElementById('modalTitle').textContent = 'Novo Professor';
            openModal('modalProfessor');
        });
    }
}, 200);

console.log('✅ professores.js carregado');