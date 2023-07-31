// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fms

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

// An FMS includeMap or excludeMap.
type PolicyIEMap struct {
	Account []string `pulumi:"account"`
	Orgunit []string `pulumi:"orgunit"`
}

// PolicyIEMapInput is an input type that accepts PolicyIEMap and PolicyIEMapOutput values.
// You can construct a concrete instance of `PolicyIEMapInput` via:
//
//	PolicyIEMap{ "key": PolicyIEArgs{...} }
type PolicyIEMapInput interface {
	pulumi.Input

	ToPolicyIEMapOutput() PolicyIEMapOutput
	ToPolicyIEMapOutputWithContext(context.Context) PolicyIEMapOutput
}

// An FMS includeMap or excludeMap.
type PolicyIEMapArgs struct {
	Account pulumi.StringArrayInput `pulumi:"account"`
	Orgunit pulumi.StringArrayInput `pulumi:"orgunit"`
}

func (PolicyIEMapArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyIEMap)(nil)).Elem()
}

func (i PolicyIEMapArgs) ToPolicyIEMapOutput() PolicyIEMapOutput {
	return i.ToPolicyIEMapOutputWithContext(context.Background())
}

func (i PolicyIEMapArgs) ToPolicyIEMapOutputWithContext(ctx context.Context) PolicyIEMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyIEMapOutput)
}

func (i PolicyIEMapArgs) ToPolicyIEMapPtrOutput() PolicyIEMapPtrOutput {
	return i.ToPolicyIEMapPtrOutputWithContext(context.Background())
}

func (i PolicyIEMapArgs) ToPolicyIEMapPtrOutputWithContext(ctx context.Context) PolicyIEMapPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyIEMapOutput).ToPolicyIEMapPtrOutputWithContext(ctx)
}

// PolicyIEMapPtrInput is an input type that accepts PolicyIEMapArgs, PolicyIEMapPtr and PolicyIEMapPtrOutput values.
// You can construct a concrete instance of `PolicyIEMapPtrInput` via:
//
//	        PolicyIEMapArgs{...}
//
//	or:
//
//	        nil
type PolicyIEMapPtrInput interface {
	pulumi.Input

	ToPolicyIEMapPtrOutput() PolicyIEMapPtrOutput
	ToPolicyIEMapPtrOutputWithContext(context.Context) PolicyIEMapPtrOutput
}

type policyIEMapPtrType PolicyIEMapArgs

func PolicyIEMapPtr(v *PolicyIEMapArgs) PolicyIEMapPtrInput {
	return (*policyIEMapPtrType)(v)
}

func (*policyIEMapPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyIEMap)(nil)).Elem()
}

func (i *policyIEMapPtrType) ToPolicyIEMapPtrOutput() PolicyIEMapPtrOutput {
	return i.ToPolicyIEMapPtrOutputWithContext(context.Background())
}

func (i *policyIEMapPtrType) ToPolicyIEMapPtrOutputWithContext(ctx context.Context) PolicyIEMapPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyIEMapPtrOutput)
}

// An FMS includeMap or excludeMap.
type PolicyIEMapOutput struct{ *pulumi.OutputState }

func (PolicyIEMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyIEMap)(nil)).Elem()
}

func (o PolicyIEMapOutput) ToPolicyIEMapOutput() PolicyIEMapOutput {
	return o
}

func (o PolicyIEMapOutput) ToPolicyIEMapOutputWithContext(ctx context.Context) PolicyIEMapOutput {
	return o
}

func (o PolicyIEMapOutput) ToPolicyIEMapPtrOutput() PolicyIEMapPtrOutput {
	return o.ToPolicyIEMapPtrOutputWithContext(context.Background())
}

func (o PolicyIEMapOutput) ToPolicyIEMapPtrOutputWithContext(ctx context.Context) PolicyIEMapPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v PolicyIEMap) *PolicyIEMap {
		return &v
	}).(PolicyIEMapPtrOutput)
}

func (o PolicyIEMapOutput) Account() pulumi.StringArrayOutput {
	return o.ApplyT(func(v PolicyIEMap) []string { return v.Account }).(pulumi.StringArrayOutput)
}

func (o PolicyIEMapOutput) Orgunit() pulumi.StringArrayOutput {
	return o.ApplyT(func(v PolicyIEMap) []string { return v.Orgunit }).(pulumi.StringArrayOutput)
}

type PolicyIEMapPtrOutput struct{ *pulumi.OutputState }

func (PolicyIEMapPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyIEMap)(nil)).Elem()
}

func (o PolicyIEMapPtrOutput) ToPolicyIEMapPtrOutput() PolicyIEMapPtrOutput {
	return o
}

func (o PolicyIEMapPtrOutput) ToPolicyIEMapPtrOutputWithContext(ctx context.Context) PolicyIEMapPtrOutput {
	return o
}

func (o PolicyIEMapPtrOutput) Elem() PolicyIEMapOutput {
	return o.ApplyT(func(v *PolicyIEMap) PolicyIEMap {
		if v != nil {
			return *v
		}
		var ret PolicyIEMap
		return ret
	}).(PolicyIEMapOutput)
}

func (o PolicyIEMapPtrOutput) Account() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *PolicyIEMap) []string {
		if v == nil {
			return nil
		}
		return v.Account
	}).(pulumi.StringArrayOutput)
}

func (o PolicyIEMapPtrOutput) Orgunit() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *PolicyIEMap) []string {
		if v == nil {
			return nil
		}
		return v.Orgunit
	}).(pulumi.StringArrayOutput)
}

// Network firewall policy.
type PolicyNetworkFirewallPolicy struct {
	FirewallDeploymentModel PolicyFirewallDeploymentModel `pulumi:"firewallDeploymentModel"`
}

// PolicyNetworkFirewallPolicyInput is an input type that accepts PolicyNetworkFirewallPolicyArgs and PolicyNetworkFirewallPolicyOutput values.
// You can construct a concrete instance of `PolicyNetworkFirewallPolicyInput` via:
//
//	PolicyNetworkFirewallPolicyArgs{...}
type PolicyNetworkFirewallPolicyInput interface {
	pulumi.Input

	ToPolicyNetworkFirewallPolicyOutput() PolicyNetworkFirewallPolicyOutput
	ToPolicyNetworkFirewallPolicyOutputWithContext(context.Context) PolicyNetworkFirewallPolicyOutput
}

// Network firewall policy.
type PolicyNetworkFirewallPolicyArgs struct {
	FirewallDeploymentModel PolicyFirewallDeploymentModelInput `pulumi:"firewallDeploymentModel"`
}

func (PolicyNetworkFirewallPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyNetworkFirewallPolicy)(nil)).Elem()
}

func (i PolicyNetworkFirewallPolicyArgs) ToPolicyNetworkFirewallPolicyOutput() PolicyNetworkFirewallPolicyOutput {
	return i.ToPolicyNetworkFirewallPolicyOutputWithContext(context.Background())
}

func (i PolicyNetworkFirewallPolicyArgs) ToPolicyNetworkFirewallPolicyOutputWithContext(ctx context.Context) PolicyNetworkFirewallPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyNetworkFirewallPolicyOutput)
}

func (i PolicyNetworkFirewallPolicyArgs) ToPolicyNetworkFirewallPolicyPtrOutput() PolicyNetworkFirewallPolicyPtrOutput {
	return i.ToPolicyNetworkFirewallPolicyPtrOutputWithContext(context.Background())
}

func (i PolicyNetworkFirewallPolicyArgs) ToPolicyNetworkFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyNetworkFirewallPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyNetworkFirewallPolicyOutput).ToPolicyNetworkFirewallPolicyPtrOutputWithContext(ctx)
}

// PolicyNetworkFirewallPolicyPtrInput is an input type that accepts PolicyNetworkFirewallPolicyArgs, PolicyNetworkFirewallPolicyPtr and PolicyNetworkFirewallPolicyPtrOutput values.
// You can construct a concrete instance of `PolicyNetworkFirewallPolicyPtrInput` via:
//
//	        PolicyNetworkFirewallPolicyArgs{...}
//
//	or:
//
//	        nil
type PolicyNetworkFirewallPolicyPtrInput interface {
	pulumi.Input

	ToPolicyNetworkFirewallPolicyPtrOutput() PolicyNetworkFirewallPolicyPtrOutput
	ToPolicyNetworkFirewallPolicyPtrOutputWithContext(context.Context) PolicyNetworkFirewallPolicyPtrOutput
}

type policyNetworkFirewallPolicyPtrType PolicyNetworkFirewallPolicyArgs

func PolicyNetworkFirewallPolicyPtr(v *PolicyNetworkFirewallPolicyArgs) PolicyNetworkFirewallPolicyPtrInput {
	return (*policyNetworkFirewallPolicyPtrType)(v)
}

func (*policyNetworkFirewallPolicyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyNetworkFirewallPolicy)(nil)).Elem()
}

func (i *policyNetworkFirewallPolicyPtrType) ToPolicyNetworkFirewallPolicyPtrOutput() PolicyNetworkFirewallPolicyPtrOutput {
	return i.ToPolicyNetworkFirewallPolicyPtrOutputWithContext(context.Background())
}

func (i *policyNetworkFirewallPolicyPtrType) ToPolicyNetworkFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyNetworkFirewallPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyNetworkFirewallPolicyPtrOutput)
}

// Network firewall policy.
type PolicyNetworkFirewallPolicyOutput struct{ *pulumi.OutputState }

func (PolicyNetworkFirewallPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyNetworkFirewallPolicy)(nil)).Elem()
}

func (o PolicyNetworkFirewallPolicyOutput) ToPolicyNetworkFirewallPolicyOutput() PolicyNetworkFirewallPolicyOutput {
	return o
}

func (o PolicyNetworkFirewallPolicyOutput) ToPolicyNetworkFirewallPolicyOutputWithContext(ctx context.Context) PolicyNetworkFirewallPolicyOutput {
	return o
}

func (o PolicyNetworkFirewallPolicyOutput) ToPolicyNetworkFirewallPolicyPtrOutput() PolicyNetworkFirewallPolicyPtrOutput {
	return o.ToPolicyNetworkFirewallPolicyPtrOutputWithContext(context.Background())
}

func (o PolicyNetworkFirewallPolicyOutput) ToPolicyNetworkFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyNetworkFirewallPolicyPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v PolicyNetworkFirewallPolicy) *PolicyNetworkFirewallPolicy {
		return &v
	}).(PolicyNetworkFirewallPolicyPtrOutput)
}

func (o PolicyNetworkFirewallPolicyOutput) FirewallDeploymentModel() PolicyFirewallDeploymentModelOutput {
	return o.ApplyT(func(v PolicyNetworkFirewallPolicy) PolicyFirewallDeploymentModel { return v.FirewallDeploymentModel }).(PolicyFirewallDeploymentModelOutput)
}

type PolicyNetworkFirewallPolicyPtrOutput struct{ *pulumi.OutputState }

func (PolicyNetworkFirewallPolicyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyNetworkFirewallPolicy)(nil)).Elem()
}

func (o PolicyNetworkFirewallPolicyPtrOutput) ToPolicyNetworkFirewallPolicyPtrOutput() PolicyNetworkFirewallPolicyPtrOutput {
	return o
}

func (o PolicyNetworkFirewallPolicyPtrOutput) ToPolicyNetworkFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyNetworkFirewallPolicyPtrOutput {
	return o
}

func (o PolicyNetworkFirewallPolicyPtrOutput) Elem() PolicyNetworkFirewallPolicyOutput {
	return o.ApplyT(func(v *PolicyNetworkFirewallPolicy) PolicyNetworkFirewallPolicy {
		if v != nil {
			return *v
		}
		var ret PolicyNetworkFirewallPolicy
		return ret
	}).(PolicyNetworkFirewallPolicyOutput)
}

func (o PolicyNetworkFirewallPolicyPtrOutput) FirewallDeploymentModel() PolicyFirewallDeploymentModelPtrOutput {
	return o.ApplyT(func(v *PolicyNetworkFirewallPolicy) *PolicyFirewallDeploymentModel {
		if v == nil {
			return nil
		}
		return &v.FirewallDeploymentModel
	}).(PolicyFirewallDeploymentModelPtrOutput)
}

// Firewall policy option.
type PolicyOption struct {
	NetworkFirewallPolicy    *PolicyNetworkFirewallPolicy    `pulumi:"networkFirewallPolicy"`
	ThirdPartyFirewallPolicy *PolicyThirdPartyFirewallPolicy `pulumi:"thirdPartyFirewallPolicy"`
}

// PolicyOptionInput is an input type that accepts PolicyOptionArgs and PolicyOptionOutput values.
// You can construct a concrete instance of `PolicyOptionInput` via:
//
//	PolicyOptionArgs{...}
type PolicyOptionInput interface {
	pulumi.Input

	ToPolicyOptionOutput() PolicyOptionOutput
	ToPolicyOptionOutputWithContext(context.Context) PolicyOptionOutput
}

// Firewall policy option.
type PolicyOptionArgs struct {
	NetworkFirewallPolicy    PolicyNetworkFirewallPolicyPtrInput    `pulumi:"networkFirewallPolicy"`
	ThirdPartyFirewallPolicy PolicyThirdPartyFirewallPolicyPtrInput `pulumi:"thirdPartyFirewallPolicy"`
}

func (PolicyOptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyOption)(nil)).Elem()
}

func (i PolicyOptionArgs) ToPolicyOptionOutput() PolicyOptionOutput {
	return i.ToPolicyOptionOutputWithContext(context.Background())
}

func (i PolicyOptionArgs) ToPolicyOptionOutputWithContext(ctx context.Context) PolicyOptionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyOptionOutput)
}

func (i PolicyOptionArgs) ToPolicyOptionPtrOutput() PolicyOptionPtrOutput {
	return i.ToPolicyOptionPtrOutputWithContext(context.Background())
}

func (i PolicyOptionArgs) ToPolicyOptionPtrOutputWithContext(ctx context.Context) PolicyOptionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyOptionOutput).ToPolicyOptionPtrOutputWithContext(ctx)
}

// PolicyOptionPtrInput is an input type that accepts PolicyOptionArgs, PolicyOptionPtr and PolicyOptionPtrOutput values.
// You can construct a concrete instance of `PolicyOptionPtrInput` via:
//
//	        PolicyOptionArgs{...}
//
//	or:
//
//	        nil
type PolicyOptionPtrInput interface {
	pulumi.Input

	ToPolicyOptionPtrOutput() PolicyOptionPtrOutput
	ToPolicyOptionPtrOutputWithContext(context.Context) PolicyOptionPtrOutput
}

type policyOptionPtrType PolicyOptionArgs

func PolicyOptionPtr(v *PolicyOptionArgs) PolicyOptionPtrInput {
	return (*policyOptionPtrType)(v)
}

func (*policyOptionPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyOption)(nil)).Elem()
}

func (i *policyOptionPtrType) ToPolicyOptionPtrOutput() PolicyOptionPtrOutput {
	return i.ToPolicyOptionPtrOutputWithContext(context.Background())
}

func (i *policyOptionPtrType) ToPolicyOptionPtrOutputWithContext(ctx context.Context) PolicyOptionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyOptionPtrOutput)
}

// Firewall policy option.
type PolicyOptionOutput struct{ *pulumi.OutputState }

func (PolicyOptionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyOption)(nil)).Elem()
}

func (o PolicyOptionOutput) ToPolicyOptionOutput() PolicyOptionOutput {
	return o
}

func (o PolicyOptionOutput) ToPolicyOptionOutputWithContext(ctx context.Context) PolicyOptionOutput {
	return o
}

func (o PolicyOptionOutput) ToPolicyOptionPtrOutput() PolicyOptionPtrOutput {
	return o.ToPolicyOptionPtrOutputWithContext(context.Background())
}

func (o PolicyOptionOutput) ToPolicyOptionPtrOutputWithContext(ctx context.Context) PolicyOptionPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v PolicyOption) *PolicyOption {
		return &v
	}).(PolicyOptionPtrOutput)
}

func (o PolicyOptionOutput) NetworkFirewallPolicy() PolicyNetworkFirewallPolicyPtrOutput {
	return o.ApplyT(func(v PolicyOption) *PolicyNetworkFirewallPolicy { return v.NetworkFirewallPolicy }).(PolicyNetworkFirewallPolicyPtrOutput)
}

func (o PolicyOptionOutput) ThirdPartyFirewallPolicy() PolicyThirdPartyFirewallPolicyPtrOutput {
	return o.ApplyT(func(v PolicyOption) *PolicyThirdPartyFirewallPolicy { return v.ThirdPartyFirewallPolicy }).(PolicyThirdPartyFirewallPolicyPtrOutput)
}

type PolicyOptionPtrOutput struct{ *pulumi.OutputState }

func (PolicyOptionPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyOption)(nil)).Elem()
}

func (o PolicyOptionPtrOutput) ToPolicyOptionPtrOutput() PolicyOptionPtrOutput {
	return o
}

func (o PolicyOptionPtrOutput) ToPolicyOptionPtrOutputWithContext(ctx context.Context) PolicyOptionPtrOutput {
	return o
}

func (o PolicyOptionPtrOutput) Elem() PolicyOptionOutput {
	return o.ApplyT(func(v *PolicyOption) PolicyOption {
		if v != nil {
			return *v
		}
		var ret PolicyOption
		return ret
	}).(PolicyOptionOutput)
}

func (o PolicyOptionPtrOutput) NetworkFirewallPolicy() PolicyNetworkFirewallPolicyPtrOutput {
	return o.ApplyT(func(v *PolicyOption) *PolicyNetworkFirewallPolicy {
		if v == nil {
			return nil
		}
		return v.NetworkFirewallPolicy
	}).(PolicyNetworkFirewallPolicyPtrOutput)
}

func (o PolicyOptionPtrOutput) ThirdPartyFirewallPolicy() PolicyThirdPartyFirewallPolicyPtrOutput {
	return o.ApplyT(func(v *PolicyOption) *PolicyThirdPartyFirewallPolicy {
		if v == nil {
			return nil
		}
		return v.ThirdPartyFirewallPolicy
	}).(PolicyThirdPartyFirewallPolicyPtrOutput)
}

// A resource tag.
type PolicyResourceTag struct {
	Key   string  `pulumi:"key"`
	Value *string `pulumi:"value"`
}

// PolicyResourceTagInput is an input type that accepts PolicyResourceTagArgs and PolicyResourceTagOutput values.
// You can construct a concrete instance of `PolicyResourceTagInput` via:
//
//	PolicyResourceTagArgs{...}
type PolicyResourceTagInput interface {
	pulumi.Input

	ToPolicyResourceTagOutput() PolicyResourceTagOutput
	ToPolicyResourceTagOutputWithContext(context.Context) PolicyResourceTagOutput
}

// A resource tag.
type PolicyResourceTagArgs struct {
	Key   pulumi.StringInput    `pulumi:"key"`
	Value pulumi.StringPtrInput `pulumi:"value"`
}

func (PolicyResourceTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyResourceTag)(nil)).Elem()
}

func (i PolicyResourceTagArgs) ToPolicyResourceTagOutput() PolicyResourceTagOutput {
	return i.ToPolicyResourceTagOutputWithContext(context.Background())
}

func (i PolicyResourceTagArgs) ToPolicyResourceTagOutputWithContext(ctx context.Context) PolicyResourceTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyResourceTagOutput)
}

// PolicyResourceTagArrayInput is an input type that accepts PolicyResourceTagArray and PolicyResourceTagArrayOutput values.
// You can construct a concrete instance of `PolicyResourceTagArrayInput` via:
//
//	PolicyResourceTagArray{ PolicyResourceTagArgs{...} }
type PolicyResourceTagArrayInput interface {
	pulumi.Input

	ToPolicyResourceTagArrayOutput() PolicyResourceTagArrayOutput
	ToPolicyResourceTagArrayOutputWithContext(context.Context) PolicyResourceTagArrayOutput
}

type PolicyResourceTagArray []PolicyResourceTagInput

func (PolicyResourceTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PolicyResourceTag)(nil)).Elem()
}

func (i PolicyResourceTagArray) ToPolicyResourceTagArrayOutput() PolicyResourceTagArrayOutput {
	return i.ToPolicyResourceTagArrayOutputWithContext(context.Background())
}

func (i PolicyResourceTagArray) ToPolicyResourceTagArrayOutputWithContext(ctx context.Context) PolicyResourceTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyResourceTagArrayOutput)
}

// A resource tag.
type PolicyResourceTagOutput struct{ *pulumi.OutputState }

func (PolicyResourceTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyResourceTag)(nil)).Elem()
}

func (o PolicyResourceTagOutput) ToPolicyResourceTagOutput() PolicyResourceTagOutput {
	return o
}

func (o PolicyResourceTagOutput) ToPolicyResourceTagOutputWithContext(ctx context.Context) PolicyResourceTagOutput {
	return o
}

func (o PolicyResourceTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v PolicyResourceTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o PolicyResourceTagOutput) Value() pulumi.StringPtrOutput {
	return o.ApplyT(func(v PolicyResourceTag) *string { return v.Value }).(pulumi.StringPtrOutput)
}

type PolicyResourceTagArrayOutput struct{ *pulumi.OutputState }

func (PolicyResourceTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PolicyResourceTag)(nil)).Elem()
}

func (o PolicyResourceTagArrayOutput) ToPolicyResourceTagArrayOutput() PolicyResourceTagArrayOutput {
	return o
}

func (o PolicyResourceTagArrayOutput) ToPolicyResourceTagArrayOutputWithContext(ctx context.Context) PolicyResourceTagArrayOutput {
	return o
}

func (o PolicyResourceTagArrayOutput) Index(i pulumi.IntInput) PolicyResourceTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PolicyResourceTag {
		return vs[0].([]PolicyResourceTag)[vs[1].(int)]
	}).(PolicyResourceTagOutput)
}

// Firewall security service policy data.
type PolicySecurityServicePolicyData struct {
	ManagedServiceData *string       `pulumi:"managedServiceData"`
	PolicyOption       *PolicyOption `pulumi:"policyOption"`
	Type               PolicyType    `pulumi:"type"`
}

// PolicySecurityServicePolicyDataInput is an input type that accepts PolicySecurityServicePolicyDataArgs and PolicySecurityServicePolicyDataOutput values.
// You can construct a concrete instance of `PolicySecurityServicePolicyDataInput` via:
//
//	PolicySecurityServicePolicyDataArgs{...}
type PolicySecurityServicePolicyDataInput interface {
	pulumi.Input

	ToPolicySecurityServicePolicyDataOutput() PolicySecurityServicePolicyDataOutput
	ToPolicySecurityServicePolicyDataOutputWithContext(context.Context) PolicySecurityServicePolicyDataOutput
}

// Firewall security service policy data.
type PolicySecurityServicePolicyDataArgs struct {
	ManagedServiceData pulumi.StringPtrInput `pulumi:"managedServiceData"`
	PolicyOption       PolicyOptionPtrInput  `pulumi:"policyOption"`
	Type               PolicyTypeInput       `pulumi:"type"`
}

func (PolicySecurityServicePolicyDataArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicySecurityServicePolicyData)(nil)).Elem()
}

func (i PolicySecurityServicePolicyDataArgs) ToPolicySecurityServicePolicyDataOutput() PolicySecurityServicePolicyDataOutput {
	return i.ToPolicySecurityServicePolicyDataOutputWithContext(context.Background())
}

func (i PolicySecurityServicePolicyDataArgs) ToPolicySecurityServicePolicyDataOutputWithContext(ctx context.Context) PolicySecurityServicePolicyDataOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicySecurityServicePolicyDataOutput)
}

// Firewall security service policy data.
type PolicySecurityServicePolicyDataOutput struct{ *pulumi.OutputState }

func (PolicySecurityServicePolicyDataOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicySecurityServicePolicyData)(nil)).Elem()
}

func (o PolicySecurityServicePolicyDataOutput) ToPolicySecurityServicePolicyDataOutput() PolicySecurityServicePolicyDataOutput {
	return o
}

func (o PolicySecurityServicePolicyDataOutput) ToPolicySecurityServicePolicyDataOutputWithContext(ctx context.Context) PolicySecurityServicePolicyDataOutput {
	return o
}

func (o PolicySecurityServicePolicyDataOutput) ManagedServiceData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v PolicySecurityServicePolicyData) *string { return v.ManagedServiceData }).(pulumi.StringPtrOutput)
}

func (o PolicySecurityServicePolicyDataOutput) PolicyOption() PolicyOptionPtrOutput {
	return o.ApplyT(func(v PolicySecurityServicePolicyData) *PolicyOption { return v.PolicyOption }).(PolicyOptionPtrOutput)
}

func (o PolicySecurityServicePolicyDataOutput) Type() PolicyTypeOutput {
	return o.ApplyT(func(v PolicySecurityServicePolicyData) PolicyType { return v.Type }).(PolicyTypeOutput)
}

type PolicySecurityServicePolicyDataPtrOutput struct{ *pulumi.OutputState }

func (PolicySecurityServicePolicyDataPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicySecurityServicePolicyData)(nil)).Elem()
}

func (o PolicySecurityServicePolicyDataPtrOutput) ToPolicySecurityServicePolicyDataPtrOutput() PolicySecurityServicePolicyDataPtrOutput {
	return o
}

func (o PolicySecurityServicePolicyDataPtrOutput) ToPolicySecurityServicePolicyDataPtrOutputWithContext(ctx context.Context) PolicySecurityServicePolicyDataPtrOutput {
	return o
}

func (o PolicySecurityServicePolicyDataPtrOutput) Elem() PolicySecurityServicePolicyDataOutput {
	return o.ApplyT(func(v *PolicySecurityServicePolicyData) PolicySecurityServicePolicyData {
		if v != nil {
			return *v
		}
		var ret PolicySecurityServicePolicyData
		return ret
	}).(PolicySecurityServicePolicyDataOutput)
}

func (o PolicySecurityServicePolicyDataPtrOutput) ManagedServiceData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PolicySecurityServicePolicyData) *string {
		if v == nil {
			return nil
		}
		return v.ManagedServiceData
	}).(pulumi.StringPtrOutput)
}

func (o PolicySecurityServicePolicyDataPtrOutput) PolicyOption() PolicyOptionPtrOutput {
	return o.ApplyT(func(v *PolicySecurityServicePolicyData) *PolicyOption {
		if v == nil {
			return nil
		}
		return v.PolicyOption
	}).(PolicyOptionPtrOutput)
}

func (o PolicySecurityServicePolicyDataPtrOutput) Type() PolicyTypePtrOutput {
	return o.ApplyT(func(v *PolicySecurityServicePolicyData) *PolicyType {
		if v == nil {
			return nil
		}
		return &v.Type
	}).(PolicyTypePtrOutput)
}

// A policy tag.
type PolicyTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// PolicyTagInput is an input type that accepts PolicyTagArgs and PolicyTagOutput values.
// You can construct a concrete instance of `PolicyTagInput` via:
//
//	PolicyTagArgs{...}
type PolicyTagInput interface {
	pulumi.Input

	ToPolicyTagOutput() PolicyTagOutput
	ToPolicyTagOutputWithContext(context.Context) PolicyTagOutput
}

// A policy tag.
type PolicyTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (PolicyTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyTag)(nil)).Elem()
}

func (i PolicyTagArgs) ToPolicyTagOutput() PolicyTagOutput {
	return i.ToPolicyTagOutputWithContext(context.Background())
}

func (i PolicyTagArgs) ToPolicyTagOutputWithContext(ctx context.Context) PolicyTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyTagOutput)
}

// PolicyTagArrayInput is an input type that accepts PolicyTagArray and PolicyTagArrayOutput values.
// You can construct a concrete instance of `PolicyTagArrayInput` via:
//
//	PolicyTagArray{ PolicyTagArgs{...} }
type PolicyTagArrayInput interface {
	pulumi.Input

	ToPolicyTagArrayOutput() PolicyTagArrayOutput
	ToPolicyTagArrayOutputWithContext(context.Context) PolicyTagArrayOutput
}

type PolicyTagArray []PolicyTagInput

func (PolicyTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PolicyTag)(nil)).Elem()
}

func (i PolicyTagArray) ToPolicyTagArrayOutput() PolicyTagArrayOutput {
	return i.ToPolicyTagArrayOutputWithContext(context.Background())
}

func (i PolicyTagArray) ToPolicyTagArrayOutputWithContext(ctx context.Context) PolicyTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyTagArrayOutput)
}

// A policy tag.
type PolicyTagOutput struct{ *pulumi.OutputState }

func (PolicyTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyTag)(nil)).Elem()
}

func (o PolicyTagOutput) ToPolicyTagOutput() PolicyTagOutput {
	return o
}

func (o PolicyTagOutput) ToPolicyTagOutputWithContext(ctx context.Context) PolicyTagOutput {
	return o
}

func (o PolicyTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v PolicyTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o PolicyTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v PolicyTag) string { return v.Value }).(pulumi.StringOutput)
}

type PolicyTagArrayOutput struct{ *pulumi.OutputState }

func (PolicyTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PolicyTag)(nil)).Elem()
}

func (o PolicyTagArrayOutput) ToPolicyTagArrayOutput() PolicyTagArrayOutput {
	return o
}

func (o PolicyTagArrayOutput) ToPolicyTagArrayOutputWithContext(ctx context.Context) PolicyTagArrayOutput {
	return o
}

func (o PolicyTagArrayOutput) Index(i pulumi.IntInput) PolicyTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PolicyTag {
		return vs[0].([]PolicyTag)[vs[1].(int)]
	}).(PolicyTagOutput)
}

// Third party firewall policy.
type PolicyThirdPartyFirewallPolicy struct {
	FirewallDeploymentModel PolicyFirewallDeploymentModel `pulumi:"firewallDeploymentModel"`
}

// PolicyThirdPartyFirewallPolicyInput is an input type that accepts PolicyThirdPartyFirewallPolicyArgs and PolicyThirdPartyFirewallPolicyOutput values.
// You can construct a concrete instance of `PolicyThirdPartyFirewallPolicyInput` via:
//
//	PolicyThirdPartyFirewallPolicyArgs{...}
type PolicyThirdPartyFirewallPolicyInput interface {
	pulumi.Input

	ToPolicyThirdPartyFirewallPolicyOutput() PolicyThirdPartyFirewallPolicyOutput
	ToPolicyThirdPartyFirewallPolicyOutputWithContext(context.Context) PolicyThirdPartyFirewallPolicyOutput
}

// Third party firewall policy.
type PolicyThirdPartyFirewallPolicyArgs struct {
	FirewallDeploymentModel PolicyFirewallDeploymentModelInput `pulumi:"firewallDeploymentModel"`
}

func (PolicyThirdPartyFirewallPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyThirdPartyFirewallPolicy)(nil)).Elem()
}

func (i PolicyThirdPartyFirewallPolicyArgs) ToPolicyThirdPartyFirewallPolicyOutput() PolicyThirdPartyFirewallPolicyOutput {
	return i.ToPolicyThirdPartyFirewallPolicyOutputWithContext(context.Background())
}

func (i PolicyThirdPartyFirewallPolicyArgs) ToPolicyThirdPartyFirewallPolicyOutputWithContext(ctx context.Context) PolicyThirdPartyFirewallPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyThirdPartyFirewallPolicyOutput)
}

func (i PolicyThirdPartyFirewallPolicyArgs) ToPolicyThirdPartyFirewallPolicyPtrOutput() PolicyThirdPartyFirewallPolicyPtrOutput {
	return i.ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(context.Background())
}

func (i PolicyThirdPartyFirewallPolicyArgs) ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyThirdPartyFirewallPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyThirdPartyFirewallPolicyOutput).ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(ctx)
}

// PolicyThirdPartyFirewallPolicyPtrInput is an input type that accepts PolicyThirdPartyFirewallPolicyArgs, PolicyThirdPartyFirewallPolicyPtr and PolicyThirdPartyFirewallPolicyPtrOutput values.
// You can construct a concrete instance of `PolicyThirdPartyFirewallPolicyPtrInput` via:
//
//	        PolicyThirdPartyFirewallPolicyArgs{...}
//
//	or:
//
//	        nil
type PolicyThirdPartyFirewallPolicyPtrInput interface {
	pulumi.Input

	ToPolicyThirdPartyFirewallPolicyPtrOutput() PolicyThirdPartyFirewallPolicyPtrOutput
	ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(context.Context) PolicyThirdPartyFirewallPolicyPtrOutput
}

type policyThirdPartyFirewallPolicyPtrType PolicyThirdPartyFirewallPolicyArgs

func PolicyThirdPartyFirewallPolicyPtr(v *PolicyThirdPartyFirewallPolicyArgs) PolicyThirdPartyFirewallPolicyPtrInput {
	return (*policyThirdPartyFirewallPolicyPtrType)(v)
}

func (*policyThirdPartyFirewallPolicyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyThirdPartyFirewallPolicy)(nil)).Elem()
}

func (i *policyThirdPartyFirewallPolicyPtrType) ToPolicyThirdPartyFirewallPolicyPtrOutput() PolicyThirdPartyFirewallPolicyPtrOutput {
	return i.ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(context.Background())
}

func (i *policyThirdPartyFirewallPolicyPtrType) ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyThirdPartyFirewallPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyThirdPartyFirewallPolicyPtrOutput)
}

// Third party firewall policy.
type PolicyThirdPartyFirewallPolicyOutput struct{ *pulumi.OutputState }

func (PolicyThirdPartyFirewallPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyThirdPartyFirewallPolicy)(nil)).Elem()
}

func (o PolicyThirdPartyFirewallPolicyOutput) ToPolicyThirdPartyFirewallPolicyOutput() PolicyThirdPartyFirewallPolicyOutput {
	return o
}

func (o PolicyThirdPartyFirewallPolicyOutput) ToPolicyThirdPartyFirewallPolicyOutputWithContext(ctx context.Context) PolicyThirdPartyFirewallPolicyOutput {
	return o
}

func (o PolicyThirdPartyFirewallPolicyOutput) ToPolicyThirdPartyFirewallPolicyPtrOutput() PolicyThirdPartyFirewallPolicyPtrOutput {
	return o.ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(context.Background())
}

func (o PolicyThirdPartyFirewallPolicyOutput) ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyThirdPartyFirewallPolicyPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v PolicyThirdPartyFirewallPolicy) *PolicyThirdPartyFirewallPolicy {
		return &v
	}).(PolicyThirdPartyFirewallPolicyPtrOutput)
}

func (o PolicyThirdPartyFirewallPolicyOutput) FirewallDeploymentModel() PolicyFirewallDeploymentModelOutput {
	return o.ApplyT(func(v PolicyThirdPartyFirewallPolicy) PolicyFirewallDeploymentModel { return v.FirewallDeploymentModel }).(PolicyFirewallDeploymentModelOutput)
}

type PolicyThirdPartyFirewallPolicyPtrOutput struct{ *pulumi.OutputState }

func (PolicyThirdPartyFirewallPolicyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyThirdPartyFirewallPolicy)(nil)).Elem()
}

func (o PolicyThirdPartyFirewallPolicyPtrOutput) ToPolicyThirdPartyFirewallPolicyPtrOutput() PolicyThirdPartyFirewallPolicyPtrOutput {
	return o
}

func (o PolicyThirdPartyFirewallPolicyPtrOutput) ToPolicyThirdPartyFirewallPolicyPtrOutputWithContext(ctx context.Context) PolicyThirdPartyFirewallPolicyPtrOutput {
	return o
}

func (o PolicyThirdPartyFirewallPolicyPtrOutput) Elem() PolicyThirdPartyFirewallPolicyOutput {
	return o.ApplyT(func(v *PolicyThirdPartyFirewallPolicy) PolicyThirdPartyFirewallPolicy {
		if v != nil {
			return *v
		}
		var ret PolicyThirdPartyFirewallPolicy
		return ret
	}).(PolicyThirdPartyFirewallPolicyOutput)
}

func (o PolicyThirdPartyFirewallPolicyPtrOutput) FirewallDeploymentModel() PolicyFirewallDeploymentModelPtrOutput {
	return o.ApplyT(func(v *PolicyThirdPartyFirewallPolicy) *PolicyFirewallDeploymentModel {
		if v == nil {
			return nil
		}
		return &v.FirewallDeploymentModel
	}).(PolicyFirewallDeploymentModelPtrOutput)
}

// A tag.
type ResourceSetTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// ResourceSetTagInput is an input type that accepts ResourceSetTagArgs and ResourceSetTagOutput values.
// You can construct a concrete instance of `ResourceSetTagInput` via:
//
//	ResourceSetTagArgs{...}
type ResourceSetTagInput interface {
	pulumi.Input

	ToResourceSetTagOutput() ResourceSetTagOutput
	ToResourceSetTagOutputWithContext(context.Context) ResourceSetTagOutput
}

// A tag.
type ResourceSetTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (ResourceSetTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceSetTag)(nil)).Elem()
}

func (i ResourceSetTagArgs) ToResourceSetTagOutput() ResourceSetTagOutput {
	return i.ToResourceSetTagOutputWithContext(context.Background())
}

func (i ResourceSetTagArgs) ToResourceSetTagOutputWithContext(ctx context.Context) ResourceSetTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResourceSetTagOutput)
}

// ResourceSetTagArrayInput is an input type that accepts ResourceSetTagArray and ResourceSetTagArrayOutput values.
// You can construct a concrete instance of `ResourceSetTagArrayInput` via:
//
//	ResourceSetTagArray{ ResourceSetTagArgs{...} }
type ResourceSetTagArrayInput interface {
	pulumi.Input

	ToResourceSetTagArrayOutput() ResourceSetTagArrayOutput
	ToResourceSetTagArrayOutputWithContext(context.Context) ResourceSetTagArrayOutput
}

type ResourceSetTagArray []ResourceSetTagInput

func (ResourceSetTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ResourceSetTag)(nil)).Elem()
}

func (i ResourceSetTagArray) ToResourceSetTagArrayOutput() ResourceSetTagArrayOutput {
	return i.ToResourceSetTagArrayOutputWithContext(context.Background())
}

func (i ResourceSetTagArray) ToResourceSetTagArrayOutputWithContext(ctx context.Context) ResourceSetTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResourceSetTagArrayOutput)
}

// A tag.
type ResourceSetTagOutput struct{ *pulumi.OutputState }

func (ResourceSetTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceSetTag)(nil)).Elem()
}

func (o ResourceSetTagOutput) ToResourceSetTagOutput() ResourceSetTagOutput {
	return o
}

func (o ResourceSetTagOutput) ToResourceSetTagOutputWithContext(ctx context.Context) ResourceSetTagOutput {
	return o
}

func (o ResourceSetTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ResourceSetTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o ResourceSetTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ResourceSetTag) string { return v.Value }).(pulumi.StringOutput)
}

type ResourceSetTagArrayOutput struct{ *pulumi.OutputState }

func (ResourceSetTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ResourceSetTag)(nil)).Elem()
}

func (o ResourceSetTagArrayOutput) ToResourceSetTagArrayOutput() ResourceSetTagArrayOutput {
	return o
}

func (o ResourceSetTagArrayOutput) ToResourceSetTagArrayOutputWithContext(ctx context.Context) ResourceSetTagArrayOutput {
	return o
}

func (o ResourceSetTagArrayOutput) Index(i pulumi.IntInput) ResourceSetTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ResourceSetTag {
		return vs[0].([]ResourceSetTag)[vs[1].(int)]
	}).(ResourceSetTagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyIEMapInput)(nil)).Elem(), PolicyIEMapArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyIEMapPtrInput)(nil)).Elem(), PolicyIEMapArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyNetworkFirewallPolicyInput)(nil)).Elem(), PolicyNetworkFirewallPolicyArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyNetworkFirewallPolicyPtrInput)(nil)).Elem(), PolicyNetworkFirewallPolicyArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyOptionInput)(nil)).Elem(), PolicyOptionArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyOptionPtrInput)(nil)).Elem(), PolicyOptionArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyResourceTagInput)(nil)).Elem(), PolicyResourceTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyResourceTagArrayInput)(nil)).Elem(), PolicyResourceTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicySecurityServicePolicyDataInput)(nil)).Elem(), PolicySecurityServicePolicyDataArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyTagInput)(nil)).Elem(), PolicyTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyTagArrayInput)(nil)).Elem(), PolicyTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyThirdPartyFirewallPolicyInput)(nil)).Elem(), PolicyThirdPartyFirewallPolicyArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyThirdPartyFirewallPolicyPtrInput)(nil)).Elem(), PolicyThirdPartyFirewallPolicyArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ResourceSetTagInput)(nil)).Elem(), ResourceSetTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ResourceSetTagArrayInput)(nil)).Elem(), ResourceSetTagArray{})
	pulumi.RegisterOutputType(PolicyIEMapOutput{})
	pulumi.RegisterOutputType(PolicyIEMapPtrOutput{})
	pulumi.RegisterOutputType(PolicyNetworkFirewallPolicyOutput{})
	pulumi.RegisterOutputType(PolicyNetworkFirewallPolicyPtrOutput{})
	pulumi.RegisterOutputType(PolicyOptionOutput{})
	pulumi.RegisterOutputType(PolicyOptionPtrOutput{})
	pulumi.RegisterOutputType(PolicyResourceTagOutput{})
	pulumi.RegisterOutputType(PolicyResourceTagArrayOutput{})
	pulumi.RegisterOutputType(PolicySecurityServicePolicyDataOutput{})
	pulumi.RegisterOutputType(PolicySecurityServicePolicyDataPtrOutput{})
	pulumi.RegisterOutputType(PolicyTagOutput{})
	pulumi.RegisterOutputType(PolicyTagArrayOutput{})
	pulumi.RegisterOutputType(PolicyThirdPartyFirewallPolicyOutput{})
	pulumi.RegisterOutputType(PolicyThirdPartyFirewallPolicyPtrOutput{})
	pulumi.RegisterOutputType(ResourceSetTagOutput{})
	pulumi.RegisterOutputType(ResourceSetTagArrayOutput{})
}
