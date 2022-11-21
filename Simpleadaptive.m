%炉の状態空間表現
a = 1 %時定数
b = 1 %適当な入力係数　
ro = ss(-1/a,b,1,0)
figure
stepplot(ro)
title('対象モデル（一次遅れ）のステップ応答')

%シム時間
d = 0.01
t = 0:d:10000;

%シム変数
dT = zeros(size(t));
KI = zeros([2 size(t,2)]);
e  = zeros(size(t));
u  = zeros(size(t));
Tr = [t(1:300000)./100.*1.3 ones(1,300000).*3000./100.*1.3 t(300000:700000)./100.*1.3];

%調整パラメータ
Gamma = diag([100 0.00]); %適応のゲイン
sigma = diag([10/a 10/a ]); %フィルタのカットオフ角振動数に相当

%シム
for n = 1:size(t,2)-1
    e(n) = dT(n) - Tr(n);
    u(n) = KI(:,n)'*[e(n) ; Tr(n)];
    dT(n+1) = dT(n) + (-1/a*dT(n) + b*(KI(:,n)'*[e(n) ; Tr(n)])^2)*d; %入力は電圧とするので二乗で入れる（若干の非線形要素）
    KI(:,n+1) = KI(:,n) + (-Gamma*[e(n) ; Tr(n)]*e(n) -sigma*KI(:,n) )*d;
end
figure
plot(t,[dT ; Tr],linewidth=2)
title('温度（青）と目標温度（橙）プロット')
ylabel('温度[Cdeg]')
xlabel('時間[s]')
figure
plot(t,KI,linewidth=2)
title('ゲインプロット')
ylabel('ゲイン')
xlabel('時間[s]')
figure
plot(t,e,linewidth=2)
title('誤差プロット')
ylabel('誤差[Cdeg]')
xlabel('時間[s]')
figure
plot(t,u,linewidth=2)
title('入力プロット')
ylabel('電圧[V]')
xlabel('時間[s]')