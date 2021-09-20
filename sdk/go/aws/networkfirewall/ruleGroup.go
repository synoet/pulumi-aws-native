// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networkfirewall

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource type definition for AWS::NetworkFirewall::RuleGroup
type RuleGroup struct {
	pulumi.CustomResourceState

	Capacity      pulumi.IntOutput            `pulumi:"capacity"`
	Description   pulumi.StringPtrOutput      `pulumi:"description"`
	RuleGroup     RuleGroupRuleGroupPtrOutput `pulumi:"ruleGroup"`
	RuleGroupArn  pulumi.StringOutput         `pulumi:"ruleGroupArn"`
	RuleGroupId   pulumi.StringOutput         `pulumi:"ruleGroupId"`
	RuleGroupName pulumi.StringOutput         `pulumi:"ruleGroupName"`
	Tags          RuleGroupTagArrayOutput     `pulumi:"tags"`
	Type          RuleGroupTypeOutput         `pulumi:"type"`
}

// NewRuleGroup registers a new resource with the given unique name, arguments, and options.
func NewRuleGroup(ctx *pulumi.Context,
	name string, args *RuleGroupArgs, opts ...pulumi.ResourceOption) (*RuleGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Capacity == nil {
		return nil, errors.New("invalid value for required argument 'Capacity'")
	}
	if args.RuleGroupName == nil {
		return nil, errors.New("invalid value for required argument 'RuleGroupName'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	var resource RuleGroup
	err := ctx.RegisterResource("aws-native:networkfirewall:RuleGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRuleGroup gets an existing RuleGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRuleGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RuleGroupState, opts ...pulumi.ResourceOption) (*RuleGroup, error) {
	var resource RuleGroup
	err := ctx.ReadResource("aws-native:networkfirewall:RuleGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RuleGroup resources.
type ruleGroupState struct {
}

type RuleGroupState struct {
}

func (RuleGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleGroupState)(nil)).Elem()
}

type ruleGroupArgs struct {
	Capacity      int                 `pulumi:"capacity"`
	Description   *string             `pulumi:"description"`
	RuleGroup     *RuleGroupRuleGroup `pulumi:"ruleGroup"`
	RuleGroupName string              `pulumi:"ruleGroupName"`
	Tags          []RuleGroupTag      `pulumi:"tags"`
	Type          RuleGroupType       `pulumi:"type"`
}

// The set of arguments for constructing a RuleGroup resource.
type RuleGroupArgs struct {
	Capacity      pulumi.IntInput
	Description   pulumi.StringPtrInput
	RuleGroup     RuleGroupRuleGroupPtrInput
	RuleGroupName pulumi.StringInput
	Tags          RuleGroupTagArrayInput
	Type          RuleGroupTypeInput
}

func (RuleGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleGroupArgs)(nil)).Elem()
}

type RuleGroupInput interface {
	pulumi.Input

	ToRuleGroupOutput() RuleGroupOutput
	ToRuleGroupOutputWithContext(ctx context.Context) RuleGroupOutput
}

func (*RuleGroup) ElementType() reflect.Type {
	return reflect.TypeOf((*RuleGroup)(nil))
}

func (i *RuleGroup) ToRuleGroupOutput() RuleGroupOutput {
	return i.ToRuleGroupOutputWithContext(context.Background())
}

func (i *RuleGroup) ToRuleGroupOutputWithContext(ctx context.Context) RuleGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RuleGroupOutput)
}

type RuleGroupOutput struct{ *pulumi.OutputState }

func (RuleGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RuleGroup)(nil))
}

func (o RuleGroupOutput) ToRuleGroupOutput() RuleGroupOutput {
	return o
}

func (o RuleGroupOutput) ToRuleGroupOutputWithContext(ctx context.Context) RuleGroupOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RuleGroupOutput{})
}
