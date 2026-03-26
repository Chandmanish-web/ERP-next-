frappe.ui.form.on('Book Transaction', {
	refresh(frm) {
		// Apply card styling to the form
		setTimeout(() => {
			$('.form-layout').addClass('transaction-card');
			$('.section-head').addClass('section-head');

			// Style status field
			if (frm.doc.status) {
				let statusClass = '';
				switch(frm.doc.status) {
					case 'Issued':
						statusClass = 'status-checked-out';
						break;
					case 'Returned':
						statusClass = 'status-available';
						break;
					case 'Overdue':
						statusClass = 'status-overdue';
						break;
				}
				$(frm.fields_dict.status.input).addClass(`status-badge ${statusClass}`);
			}

			// Style transaction type
			if (frm.doc.transaction_type) {
				let typeColor = frm.doc.transaction_type === 'Issue' ? '#fd7e14' : '#28a745';
				$(frm.fields_dict.transaction_type.input).css('border-left', `4px solid ${typeColor}`);
			}

			// Style form controls
			$('.form-control').addClass('form-control');
			$('.select-field').addClass('select-field');

			// Add transaction indicator
			if (frm.doc.transaction_id) {
				frm.dashboard.add_indicator(__('Transaction: {0}', [frm.doc.transaction_id]), 'green');
			}
		}, 100);
	},

	status(frm) {
		// Update status styling when status changes
		let statusClass = '';
		switch(frm.doc.status) {
			case 'Issued':
				statusClass = 'status-checked-out';
				break;
			case 'Returned':
				statusClass = 'status-available';
				break;
			case 'Overdue':
				statusClass = 'status-overdue';
				break;
		}
		$(frm.fields_dict.status.input).removeClass('status-available status-checked-out status-overdue').addClass(`status-badge ${statusClass}`);
	},

	transaction_type(frm) {
		// Update transaction type styling
		let typeColor = frm.doc.transaction_type === 'Issue' ? '#fd7e14' : '#28a745';
		$(frm.fields_dict.transaction_type.input).css('border-left', `4px solid ${typeColor}`);
	}
});