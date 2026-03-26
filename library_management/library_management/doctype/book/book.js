frappe.ui.form.on('Book', {
	refresh(frm) {
		// Apply card styling to the form
		setTimeout(() => {
			$('.form-layout').addClass('book-card');
			$('.section-head').addClass('section-head');

			// Style status field
			if (frm.doc.status) {
				let statusClass = '';
				switch(frm.doc.status) {
					case 'Available':
						statusClass = 'status-available';
						break;
					case 'Checked Out':
						statusClass = 'status-checked-out';
						break;
					case 'Maintenance':
						statusClass = 'status-maintenance';
						break;
				}
				$(frm.fields_dict.status.input).addClass(`status-badge ${statusClass}`);
			}

			// Add hover effects to image fields
			$('.img-field').addClass('img-field');

			// Style form controls
			$('.form-control').addClass('form-control');
			$('.select-field').addClass('select-field');
		}, 100);
	},

	status(frm) {
		// Update status styling when status changes
		let statusClass = '';
		switch(frm.doc.status) {
			case 'Available':
				statusClass = 'status-available';
				break;
			case 'Checked Out':
				statusClass = 'status-checked-out';
				break;
			case 'Maintenance':
				statusClass = 'status-maintenance';
				break;
		}
		$(frm.fields_dict.status.input).removeClass('status-available status-checked-out status-maintenance').addClass(`status-badge ${statusClass}`);
	}
});