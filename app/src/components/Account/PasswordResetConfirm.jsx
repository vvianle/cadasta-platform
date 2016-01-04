import React from 'react';
import { connect } from 'react-redux';

import * as accountActions from '../../actions/account';


export const PasswordResetConfirm = React.createClass({
  handleFormSubmit: function(e) {
    e.preventDefault();
    this.props.accountResetConfirmPassword({
      new_password: this.refs.new_password.value,
      re_new_password: this.refs.re_new_password.value,
      uid: this.props.params.uid,
      token: this.props.params.token
    })
  },

  render: function() {
    return (
      <form onSubmit={this.handleFormSubmit}>
        <label htmlFor="new_password">Enter new password</label>
        <input type="password" name="new_password" ref="new_password" />

        <label htmlFor="re_new_password">Retype newpassword</label>
        <input type="password" name="re_new_password" ref="re_new_password" />

        <button type="submit">Reset password</button>
      </form>
    )
  }
});

function mapStateToProps(state) {
  return {};
}


export const PasswordResetConfirmContainer = connect(
  mapStateToProps,
  accountActions
)(PasswordResetConfirm);