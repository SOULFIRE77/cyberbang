
import { TonConnectButton } from '@tonconnect/ui-react';

export default function Home() {
  return (
    <div style={{ padding: 40 }}>
      <h1>Cyberbang</h1>
      <TonConnectButton />
      <p>Подключи TON кошелёк и получи NFT!</p>
    </div>
  );
}
