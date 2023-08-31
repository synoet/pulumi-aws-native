// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cognito

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Cognito::UserPoolUser
//
// Deprecated: UserPoolUser is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type UserPoolUser struct {
	pulumi.CustomResourceState

	ClientMetadata         pulumi.AnyOutput                     `pulumi:"clientMetadata"`
	DesiredDeliveryMediums pulumi.StringArrayOutput             `pulumi:"desiredDeliveryMediums"`
	ForceAliasCreation     pulumi.BoolPtrOutput                 `pulumi:"forceAliasCreation"`
	MessageAction          pulumi.StringPtrOutput               `pulumi:"messageAction"`
	UserAttributes         UserPoolUserAttributeTypeArrayOutput `pulumi:"userAttributes"`
	UserPoolId             pulumi.StringOutput                  `pulumi:"userPoolId"`
	Username               pulumi.StringPtrOutput               `pulumi:"username"`
	ValidationData         UserPoolUserAttributeTypeArrayOutput `pulumi:"validationData"`
}

// NewUserPoolUser registers a new resource with the given unique name, arguments, and options.
func NewUserPoolUser(ctx *pulumi.Context,
	name string, args *UserPoolUserArgs, opts ...pulumi.ResourceOption) (*UserPoolUser, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.UserPoolId == nil {
		return nil, errors.New("invalid value for required argument 'UserPoolId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"clientMetadata",
		"desiredDeliveryMediums[*]",
		"forceAliasCreation",
		"messageAction",
		"userAttributes[*]",
		"userPoolId",
		"username",
		"validationData[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource UserPoolUser
	err := ctx.RegisterResource("aws-native:cognito:UserPoolUser", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPoolUser gets an existing UserPoolUser resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPoolUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPoolUserState, opts ...pulumi.ResourceOption) (*UserPoolUser, error) {
	var resource UserPoolUser
	err := ctx.ReadResource("aws-native:cognito:UserPoolUser", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPoolUser resources.
type userPoolUserState struct {
}

type UserPoolUserState struct {
}

func (UserPoolUserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolUserState)(nil)).Elem()
}

type userPoolUserArgs struct {
	ClientMetadata         interface{}                 `pulumi:"clientMetadata"`
	DesiredDeliveryMediums []string                    `pulumi:"desiredDeliveryMediums"`
	ForceAliasCreation     *bool                       `pulumi:"forceAliasCreation"`
	MessageAction          *string                     `pulumi:"messageAction"`
	UserAttributes         []UserPoolUserAttributeType `pulumi:"userAttributes"`
	UserPoolId             string                      `pulumi:"userPoolId"`
	Username               *string                     `pulumi:"username"`
	ValidationData         []UserPoolUserAttributeType `pulumi:"validationData"`
}

// The set of arguments for constructing a UserPoolUser resource.
type UserPoolUserArgs struct {
	ClientMetadata         pulumi.Input
	DesiredDeliveryMediums pulumi.StringArrayInput
	ForceAliasCreation     pulumi.BoolPtrInput
	MessageAction          pulumi.StringPtrInput
	UserAttributes         UserPoolUserAttributeTypeArrayInput
	UserPoolId             pulumi.StringInput
	Username               pulumi.StringPtrInput
	ValidationData         UserPoolUserAttributeTypeArrayInput
}

func (UserPoolUserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolUserArgs)(nil)).Elem()
}

type UserPoolUserInput interface {
	pulumi.Input

	ToUserPoolUserOutput() UserPoolUserOutput
	ToUserPoolUserOutputWithContext(ctx context.Context) UserPoolUserOutput
}

func (*UserPoolUser) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolUser)(nil)).Elem()
}

func (i *UserPoolUser) ToUserPoolUserOutput() UserPoolUserOutput {
	return i.ToUserPoolUserOutputWithContext(context.Background())
}

func (i *UserPoolUser) ToUserPoolUserOutputWithContext(ctx context.Context) UserPoolUserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPoolUserOutput)
}

type UserPoolUserOutput struct{ *pulumi.OutputState }

func (UserPoolUserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserPoolUser)(nil)).Elem()
}

func (o UserPoolUserOutput) ToUserPoolUserOutput() UserPoolUserOutput {
	return o
}

func (o UserPoolUserOutput) ToUserPoolUserOutputWithContext(ctx context.Context) UserPoolUserOutput {
	return o
}

func (o UserPoolUserOutput) ClientMetadata() pulumi.AnyOutput {
	return o.ApplyT(func(v *UserPoolUser) pulumi.AnyOutput { return v.ClientMetadata }).(pulumi.AnyOutput)
}

func (o UserPoolUserOutput) DesiredDeliveryMediums() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *UserPoolUser) pulumi.StringArrayOutput { return v.DesiredDeliveryMediums }).(pulumi.StringArrayOutput)
}

func (o UserPoolUserOutput) ForceAliasCreation() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *UserPoolUser) pulumi.BoolPtrOutput { return v.ForceAliasCreation }).(pulumi.BoolPtrOutput)
}

func (o UserPoolUserOutput) MessageAction() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *UserPoolUser) pulumi.StringPtrOutput { return v.MessageAction }).(pulumi.StringPtrOutput)
}

func (o UserPoolUserOutput) UserAttributes() UserPoolUserAttributeTypeArrayOutput {
	return o.ApplyT(func(v *UserPoolUser) UserPoolUserAttributeTypeArrayOutput { return v.UserAttributes }).(UserPoolUserAttributeTypeArrayOutput)
}

func (o UserPoolUserOutput) UserPoolId() pulumi.StringOutput {
	return o.ApplyT(func(v *UserPoolUser) pulumi.StringOutput { return v.UserPoolId }).(pulumi.StringOutput)
}

func (o UserPoolUserOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *UserPoolUser) pulumi.StringPtrOutput { return v.Username }).(pulumi.StringPtrOutput)
}

func (o UserPoolUserOutput) ValidationData() UserPoolUserAttributeTypeArrayOutput {
	return o.ApplyT(func(v *UserPoolUser) UserPoolUserAttributeTypeArrayOutput { return v.ValidationData }).(UserPoolUserAttributeTypeArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserPoolUserInput)(nil)).Elem(), &UserPoolUser{})
	pulumi.RegisterOutputType(UserPoolUserOutput{})
}
