carregarCursos();

async function carregarCursos() {
    const lista = document.getElementById('listaCursos');
    if (!lista) return;
    
    showLoading(lista);
    
    try {
        const response = await fetch(`${API_BASE_URL}/cursos`);
        const cursos = await response.json();
        
        if (cursos.error) {
            lista.innerHTML = `<p style="color: red;">Erro: ${cursos.error}</p>`;
            return;
        }
        
        if (cursos.length === 0) {
            lista.innerHTML = '<p>Nenhum curso cadastrado.</p>';
            return;
        }
        
        let html = `
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Código</th>
                        <th>Carga Horária</th>
                        <th>Descrição</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
        `;
        
        cursos.forEach(curso => {
            const desc = curso.descricao ? (curso.descricao.substring(0, 50) + '...') : '-';
            html += `
                <tr>
                    <td>${curso.nome}</td>
                    <td>${curso.codigo}</td>
                    <td>${curso.carga_horaria}h</td>
                    <td>${desc}</td>
                    <td>
                        <button class="btn-edit" onclick="editarCurso(${curso.id})">Editar</button>
                        <button class="btn-delete" onclick="excluirCurso(${curso.id}, '${curso.nome.replace(/'/g, "\\'")}')">Excluir</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        lista.innerHTML = html;
    } catch (error) {
        console.error('Erro:', error);
        lista.innerHTML = '<p style="color: red;">Erro ao carregar cursos.</p>';
    }
}

async function salvarCurso(event) {
    event.preventDefault();
    
    const id = document.getElementById('cursoId').value;
    const data = {
        nome: document.getElementById('nome').value,
        codigo: document.getElementById('codigo').value,
        carga_horaria: parseInt(document.getElementById('carga_horaria').value),
        descricao: document.getElementById('descricao').value
    };
    
    try {
        let response;
        if (id) {
            response = await fetch(`${API_BASE_URL}/cursos/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        } else {
            response = await fetch(`${API_BASE_URL}/cursos`, {
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
        
        showAlert(id ? 'Curso atualizado!' : 'Curso cadastrado!');
        closeModal('modalCurso');
        document.getElementById('formCurso').reset();
        carregarCursos();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao salvar curso', 'error');
    }
}

async function editarCurso(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/cursos/${id}`);
        const curso = await response.json();
        
        if (curso.error) {
            showAlert(curso.error, 'error');
            return;
        }
        
        document.getElementById('modalTitle').textContent = 'Editar Curso';
        document.getElementById('cursoId').value = curso.id;
        document.getElementById('nome').value = curso.nome;
        document.getElementById('codigo').value = curso.codigo;
        document.getElementById('carga_horaria').value = curso.carga_horaria;
        document.getElementById('descricao').value = curso.descricao || '';
        
        openModal('modalCurso');
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao carregar curso', 'error');
    }
}

async function excluirCurso(id, nome) {
    const result = await Swal.fire({
        title: 'Tem certeza?',
        text: `Deseja excluir o curso de ${nome}?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Cancelar'
    });

    if (!result.isConfirmed) return;

    try {
        const response = await fetch(`${API_BASE_URL}/cursos/${id}`, { method: 'DELETE' });
        const result = await response.json();

        if (result.error) {
            Swal.fire('Erro!', result.error, 'error');
            return;
        }

        Swal.fire('Excluído!', 'Curso removido.', 'success');
        carregarCursos();
    } catch (error) {
        console.error('Erro:', error);
        Swal.fire('Erro!', 'Erro de conexão.', 'error');
    }
}

setTimeout(() => {
    const btnNovo = document.querySelector('.btn-primary');
    if (btnNovo) {
        const newBtn = btnNovo.cloneNode(true);
        btnNovo.parentNode.replaceChild(newBtn, btnNovo);
        newBtn.addEventListener('click', () => {
            document.getElementById('formCurso').reset();
            document.getElementById('cursoId').value = '';
            document.getElementById('modalTitle').textContent = 'Novo Curso';
        });
    }
}, 200);

console.log('✅ cursos.js carregado');