import { UUID } from "crypto";
import { useState } from "react";

export const useLocalStorage = () => {
  const [card, setCard] = useState<UUID | null>(() => {
    try {
      const local_card = window.localStorage.getItem("card");
      return local_card ? (JSON.parse(local_card) as UUID) : null;
    } catch (error) {
      return null;
    }
  });

  const updateCard = (card_uuid: UUID) => {
    setCard(card_uuid);
    window.localStorage.setItem("card", JSON.stringify(card));
  };

  const deleteCard = () => {
    setCard(null);
    window.localStorage.removeItem("card");
  };

  return { card, updateCard, deleteCard };
};
