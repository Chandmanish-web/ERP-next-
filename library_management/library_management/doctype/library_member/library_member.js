frappe.ui.form.on('Library Member', {
	refresh(frm) {
		// Apply card styling to the form
		setTimeout(() => {
			$('.form-layout').addClass('member-card');
			$('.section-head').addClass('section-head');

			// Style membership type with colors
			if (frm.doc.membership_type) {
				let typeColor = '';
				switch(frm.doc.membership_type) {
					case 'Standard':
						typeColor = '#28a745';
						break;
					case 'Premium':
						typeColor = '#fd7e14';
						break;
					case 'VIP':
						typeColor = '#dc3545';
						break;
				}
				$(frm.fields_dict.membership_type.input).css('border-left', `4px solid ${typeColor}`);
			}

			// Style form controls
			$('.form-control').addClass('form-control');
			$('.select-field').addClass('select-field');

			// Add member statistics if available
			if (frm.doc.member_id) {
				frm.dashboard.add_indicator(__('Member ID: {0}', [frm.doc.member_id]), 'blue');
			}
		}, 100);
	},

	membership_type(frm) {
		// Update membership type styling
		let typeColor = '';
		switch(frm.doc.membership_type) {
			case 'Standard':
				typeColor = '#28a745';
				break;
			case 'Premium':
				typeColor = '#fd7e14';
				break;
			case 'VIP':
				typeColor = '#dc3545';
				break;
		}
		$(frm.fields_dict.membership_type.input).css('border-left', `4px solid ${typeColor}`);
	}
});