import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";

import RecipeBox from "./RecipeBox";

const MainDiv = styled.div`
  padding-top: 3rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
`;

const RecipeList = ({ recipes }) => {
  return (
    <MainDiv>
      {recipes.map((recipe, index) => (
        <RecipeBox key={index} recipe={recipe} />
      ))}
    </MainDiv>
  );
};

RecipeList.propTypes = {};

export default RecipeList;
