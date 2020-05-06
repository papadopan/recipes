import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";

import Logo from "./Logo";
import Menu from "./Menu";

const HeaderDiv = styled.div`
  height: 4em;
  width: 100%;
  background: var(--color-main);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
`;

const Header = (props) => {
  return (
    <HeaderDiv>
      <Logo />
      <Menu />
    </HeaderDiv>
  );
};

Header.propTypes = {};

export default Header;
