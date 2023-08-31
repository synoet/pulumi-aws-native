// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package billingconductor

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.
//
// Deprecated: PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type PricingRule struct {
	pulumi.CustomResourceState

	// Pricing rule ARN
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The number of pricing plans associated with pricing rule
	AssociatedPricingPlanCount pulumi.IntOutput `pulumi:"associatedPricingPlanCount"`
	// The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
	BillingEntity PricingRuleBillingEntityPtrOutput `pulumi:"billingEntity"`
	// Creation timestamp in UNIX epoch time format
	CreationTime pulumi.IntOutput `pulumi:"creationTime"`
	// Pricing rule description
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Latest modified timestamp in UNIX epoch time format
	LastModifiedTime pulumi.IntOutput `pulumi:"lastModifiedTime"`
	// Pricing rule modifier percentage
	ModifierPercentage pulumi.Float64PtrOutput `pulumi:"modifierPercentage"`
	// Pricing rule name
	Name pulumi.StringOutput `pulumi:"name"`
	// The Operation which a SKU pricing rule is modifying
	Operation pulumi.StringPtrOutput `pulumi:"operation"`
	// A term used to categorize the granularity of a Pricing Rule.
	Scope PricingRuleScopeOutput `pulumi:"scope"`
	// The service which a pricing rule is applied on
	Service pulumi.StringPtrOutput    `pulumi:"service"`
	Tags    PricingRuleTagArrayOutput `pulumi:"tags"`
	// The set of tiering configurations for the pricing rule.
	Tiering TieringPropertiesPtrOutput `pulumi:"tiering"`
	// One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
	Type PricingRuleTypeOutput `pulumi:"type"`
	// The UsageType which a SKU pricing rule is modifying
	UsageType pulumi.StringPtrOutput `pulumi:"usageType"`
}

// NewPricingRule registers a new resource with the given unique name, arguments, and options.
func NewPricingRule(ctx *pulumi.Context,
	name string, args *PricingRuleArgs, opts ...pulumi.ResourceOption) (*PricingRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Scope == nil {
		return nil, errors.New("invalid value for required argument 'Scope'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"billingEntity",
		"operation",
		"scope",
		"service",
		"usageType",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource PricingRule
	err := ctx.RegisterResource("aws-native:billingconductor:PricingRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPricingRule gets an existing PricingRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPricingRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PricingRuleState, opts ...pulumi.ResourceOption) (*PricingRule, error) {
	var resource PricingRule
	err := ctx.ReadResource("aws-native:billingconductor:PricingRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PricingRule resources.
type pricingRuleState struct {
}

type PricingRuleState struct {
}

func (PricingRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*pricingRuleState)(nil)).Elem()
}

type pricingRuleArgs struct {
	// The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
	BillingEntity *PricingRuleBillingEntity `pulumi:"billingEntity"`
	// Pricing rule description
	Description *string `pulumi:"description"`
	// Pricing rule modifier percentage
	ModifierPercentage *float64 `pulumi:"modifierPercentage"`
	// Pricing rule name
	Name *string `pulumi:"name"`
	// The Operation which a SKU pricing rule is modifying
	Operation *string `pulumi:"operation"`
	// A term used to categorize the granularity of a Pricing Rule.
	Scope PricingRuleScope `pulumi:"scope"`
	// The service which a pricing rule is applied on
	Service *string          `pulumi:"service"`
	Tags    []PricingRuleTag `pulumi:"tags"`
	// The set of tiering configurations for the pricing rule.
	Tiering *TieringProperties `pulumi:"tiering"`
	// One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
	Type PricingRuleType `pulumi:"type"`
	// The UsageType which a SKU pricing rule is modifying
	UsageType *string `pulumi:"usageType"`
}

// The set of arguments for constructing a PricingRule resource.
type PricingRuleArgs struct {
	// The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
	BillingEntity PricingRuleBillingEntityPtrInput
	// Pricing rule description
	Description pulumi.StringPtrInput
	// Pricing rule modifier percentage
	ModifierPercentage pulumi.Float64PtrInput
	// Pricing rule name
	Name pulumi.StringPtrInput
	// The Operation which a SKU pricing rule is modifying
	Operation pulumi.StringPtrInput
	// A term used to categorize the granularity of a Pricing Rule.
	Scope PricingRuleScopeInput
	// The service which a pricing rule is applied on
	Service pulumi.StringPtrInput
	Tags    PricingRuleTagArrayInput
	// The set of tiering configurations for the pricing rule.
	Tiering TieringPropertiesPtrInput
	// One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
	Type PricingRuleTypeInput
	// The UsageType which a SKU pricing rule is modifying
	UsageType pulumi.StringPtrInput
}

func (PricingRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pricingRuleArgs)(nil)).Elem()
}

type PricingRuleInput interface {
	pulumi.Input

	ToPricingRuleOutput() PricingRuleOutput
	ToPricingRuleOutputWithContext(ctx context.Context) PricingRuleOutput
}

func (*PricingRule) ElementType() reflect.Type {
	return reflect.TypeOf((**PricingRule)(nil)).Elem()
}

func (i *PricingRule) ToPricingRuleOutput() PricingRuleOutput {
	return i.ToPricingRuleOutputWithContext(context.Background())
}

func (i *PricingRule) ToPricingRuleOutputWithContext(ctx context.Context) PricingRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PricingRuleOutput)
}

type PricingRuleOutput struct{ *pulumi.OutputState }

func (PricingRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PricingRule)(nil)).Elem()
}

func (o PricingRuleOutput) ToPricingRuleOutput() PricingRuleOutput {
	return o
}

func (o PricingRuleOutput) ToPricingRuleOutputWithContext(ctx context.Context) PricingRuleOutput {
	return o
}

// Pricing rule ARN
func (o PricingRuleOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The number of pricing plans associated with pricing rule
func (o PricingRuleOutput) AssociatedPricingPlanCount() pulumi.IntOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.IntOutput { return v.AssociatedPricingPlanCount }).(pulumi.IntOutput)
}

// The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
func (o PricingRuleOutput) BillingEntity() PricingRuleBillingEntityPtrOutput {
	return o.ApplyT(func(v *PricingRule) PricingRuleBillingEntityPtrOutput { return v.BillingEntity }).(PricingRuleBillingEntityPtrOutput)
}

// Creation timestamp in UNIX epoch time format
func (o PricingRuleOutput) CreationTime() pulumi.IntOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.IntOutput { return v.CreationTime }).(pulumi.IntOutput)
}

// Pricing rule description
func (o PricingRuleOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Latest modified timestamp in UNIX epoch time format
func (o PricingRuleOutput) LastModifiedTime() pulumi.IntOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.IntOutput { return v.LastModifiedTime }).(pulumi.IntOutput)
}

// Pricing rule modifier percentage
func (o PricingRuleOutput) ModifierPercentage() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.Float64PtrOutput { return v.ModifierPercentage }).(pulumi.Float64PtrOutput)
}

// Pricing rule name
func (o PricingRuleOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The Operation which a SKU pricing rule is modifying
func (o PricingRuleOutput) Operation() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.StringPtrOutput { return v.Operation }).(pulumi.StringPtrOutput)
}

// A term used to categorize the granularity of a Pricing Rule.
func (o PricingRuleOutput) Scope() PricingRuleScopeOutput {
	return o.ApplyT(func(v *PricingRule) PricingRuleScopeOutput { return v.Scope }).(PricingRuleScopeOutput)
}

// The service which a pricing rule is applied on
func (o PricingRuleOutput) Service() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.StringPtrOutput { return v.Service }).(pulumi.StringPtrOutput)
}

func (o PricingRuleOutput) Tags() PricingRuleTagArrayOutput {
	return o.ApplyT(func(v *PricingRule) PricingRuleTagArrayOutput { return v.Tags }).(PricingRuleTagArrayOutput)
}

// The set of tiering configurations for the pricing rule.
func (o PricingRuleOutput) Tiering() TieringPropertiesPtrOutput {
	return o.ApplyT(func(v *PricingRule) TieringPropertiesPtrOutput { return v.Tiering }).(TieringPropertiesPtrOutput)
}

// One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
func (o PricingRuleOutput) Type() PricingRuleTypeOutput {
	return o.ApplyT(func(v *PricingRule) PricingRuleTypeOutput { return v.Type }).(PricingRuleTypeOutput)
}

// The UsageType which a SKU pricing rule is modifying
func (o PricingRuleOutput) UsageType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PricingRule) pulumi.StringPtrOutput { return v.UsageType }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PricingRuleInput)(nil)).Elem(), &PricingRule{})
	pulumi.RegisterOutputType(PricingRuleOutput{})
}
