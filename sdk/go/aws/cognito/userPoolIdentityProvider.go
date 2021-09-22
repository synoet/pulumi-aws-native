// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cognito

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Cognito::UserPoolIdentityProvider
//
// Deprecated: UserPoolIdentityProvider is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type UserPoolIdentityProvider struct {
	pulumi.CustomResourceState

	AttributeMapping pulumi.AnyOutput         `pulumi:"attributeMapping"`
	IdpIdentifiers   pulumi.StringArrayOutput `pulumi:"idpIdentifiers"`
	ProviderDetails  pulumi.AnyOutput         `pulumi:"providerDetails"`
	ProviderName     pulumi.StringOutput      `pulumi:"providerName"`
	ProviderType     pulumi.StringOutput      `pulumi:"providerType"`
	UserPoolId       pulumi.StringOutput      `pulumi:"userPoolId"`
}

// NewUserPoolIdentityProvider registers a new resource with the given unique name, arguments, and options.
func NewUserPoolIdentityProvider(ctx *pulumi.Context,
	name string, args *UserPoolIdentityProviderArgs, opts ...pulumi.ResourceOption) (*UserPoolIdentityProvider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProviderName == nil {
		return nil, errors.New("invalid value for required argument 'ProviderName'")
	}
	if args.ProviderType == nil {
		return nil, errors.New("invalid value for required argument 'ProviderType'")
	}
	if args.UserPoolId == nil {
		return nil, errors.New("invalid value for required argument 'UserPoolId'")
	}
	var resource UserPoolIdentityProvider
	err := ctx.RegisterResource("aws-native:cognito:UserPoolIdentityProvider", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPoolIdentityProvider gets an existing UserPoolIdentityProvider resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPoolIdentityProvider(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPoolIdentityProviderState, opts ...pulumi.ResourceOption) (*UserPoolIdentityProvider, error) {
	var resource UserPoolIdentityProvider
	err := ctx.ReadResource("aws-native:cognito:UserPoolIdentityProvider", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPoolIdentityProvider resources.
type userPoolIdentityProviderState struct {
}

type UserPoolIdentityProviderState struct {
}

func (UserPoolIdentityProviderState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolIdentityProviderState)(nil)).Elem()
}

type userPoolIdentityProviderArgs struct {
	AttributeMapping interface{} `pulumi:"attributeMapping"`
	IdpIdentifiers   []string    `pulumi:"idpIdentifiers"`
	ProviderDetails  interface{} `pulumi:"providerDetails"`
	ProviderName     string      `pulumi:"providerName"`
	ProviderType     string      `pulumi:"providerType"`
	UserPoolId       string      `pulumi:"userPoolId"`
}

// The set of arguments for constructing a UserPoolIdentityProvider resource.
type UserPoolIdentityProviderArgs struct {
	AttributeMapping pulumi.Input
	IdpIdentifiers   pulumi.StringArrayInput
	ProviderDetails  pulumi.Input
	ProviderName     pulumi.StringInput
	ProviderType     pulumi.StringInput
	UserPoolId       pulumi.StringInput
}

func (UserPoolIdentityProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPoolIdentityProviderArgs)(nil)).Elem()
}

type UserPoolIdentityProviderInput interface {
	pulumi.Input

	ToUserPoolIdentityProviderOutput() UserPoolIdentityProviderOutput
	ToUserPoolIdentityProviderOutputWithContext(ctx context.Context) UserPoolIdentityProviderOutput
}

func (*UserPoolIdentityProvider) ElementType() reflect.Type {
	return reflect.TypeOf((*UserPoolIdentityProvider)(nil))
}

func (i *UserPoolIdentityProvider) ToUserPoolIdentityProviderOutput() UserPoolIdentityProviderOutput {
	return i.ToUserPoolIdentityProviderOutputWithContext(context.Background())
}

func (i *UserPoolIdentityProvider) ToUserPoolIdentityProviderOutputWithContext(ctx context.Context) UserPoolIdentityProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPoolIdentityProviderOutput)
}

type UserPoolIdentityProviderOutput struct{ *pulumi.OutputState }

func (UserPoolIdentityProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserPoolIdentityProvider)(nil))
}

func (o UserPoolIdentityProviderOutput) ToUserPoolIdentityProviderOutput() UserPoolIdentityProviderOutput {
	return o
}

func (o UserPoolIdentityProviderOutput) ToUserPoolIdentityProviderOutputWithContext(ctx context.Context) UserPoolIdentityProviderOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(UserPoolIdentityProviderOutput{})
}
