import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";
import { Link } from "react-router-dom";

import RecipeStats from "./RecipeStats";

const SLink = styled(Link)`
  color: var(--color-black);
  flex-direction: row;
  display: flex;
  height: 100%;
  width: 100%;

  &:hover {
    color: black;
  }
`;

const MainDiv = styled.div`
  box-shadow: 2px 8px 16px rgba(24, 50, 115, 0.2);
  width: 100%;
  max-width: 320px;
  height: 120px;
  border-radius: 5px;
  margin: 1em;
  padding: 0.5em;
`;

const H1 = styled.h1`
  color: var(--color-white);
  font-weight: 600;
  margin-left: 1em;
  color: black;
`;

const Stats = styled.div`
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding: 0 0.7em;
`;

const ImagedDiv = styled.div`
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.3),
      rgba(0, 0, 0, 0.3)
    ),
    url("https://images.unsplash.com/photo-1563379926898-05f4575a45d8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80");
  height: 100%;
  width: 120px;

  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  padding: 1em;
  border-radius: 5px;
`;

const Div = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
`;

const RecipeBox = ({ recipe }) => {
  return (
    <MainDiv>
      <SLink to={`/recipe/${recipe.id}`}>
        <ImagedDiv></ImagedDiv>
        <Div>
          <H1>{recipe.title}</H1>
          <Stats>
            <RecipeStats icon="time" label={`${recipe.time} mins`} />
            <RecipeStats icon="category" label={recipe.category} />
            <RecipeStats
              icon="portion"
              label={`${recipe.portions} portion(s)`}
            />
          </Stats>
        </Div>
      </SLink>
    </MainDiv>
  );
};

RecipeBox.propTypes = {};

export default RecipeBox;
