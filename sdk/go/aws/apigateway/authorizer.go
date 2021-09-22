// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ApiGateway::Authorizer
//
// Deprecated: Authorizer is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Authorizer struct {
	pulumi.CustomResourceState

	AuthType                     pulumi.StringPtrOutput   `pulumi:"authType"`
	AuthorizerCredentials        pulumi.StringPtrOutput   `pulumi:"authorizerCredentials"`
	AuthorizerResultTtlInSeconds pulumi.IntPtrOutput      `pulumi:"authorizerResultTtlInSeconds"`
	AuthorizerUri                pulumi.StringPtrOutput   `pulumi:"authorizerUri"`
	IdentitySource               pulumi.StringPtrOutput   `pulumi:"identitySource"`
	IdentityValidationExpression pulumi.StringPtrOutput   `pulumi:"identityValidationExpression"`
	Name                         pulumi.StringPtrOutput   `pulumi:"name"`
	ProviderARNs                 pulumi.StringArrayOutput `pulumi:"providerARNs"`
	RestApiId                    pulumi.StringOutput      `pulumi:"restApiId"`
	Type                         pulumi.StringOutput      `pulumi:"type"`
}

// NewAuthorizer registers a new resource with the given unique name, arguments, and options.
func NewAuthorizer(ctx *pulumi.Context,
	name string, args *AuthorizerArgs, opts ...pulumi.ResourceOption) (*Authorizer, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RestApiId == nil {
		return nil, errors.New("invalid value for required argument 'RestApiId'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	var resource Authorizer
	err := ctx.RegisterResource("aws-native:apigateway:Authorizer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAuthorizer gets an existing Authorizer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAuthorizer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AuthorizerState, opts ...pulumi.ResourceOption) (*Authorizer, error) {
	var resource Authorizer
	err := ctx.ReadResource("aws-native:apigateway:Authorizer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Authorizer resources.
type authorizerState struct {
}

type AuthorizerState struct {
}

func (AuthorizerState) ElementType() reflect.Type {
	return reflect.TypeOf((*authorizerState)(nil)).Elem()
}

type authorizerArgs struct {
	AuthType                     *string  `pulumi:"authType"`
	AuthorizerCredentials        *string  `pulumi:"authorizerCredentials"`
	AuthorizerResultTtlInSeconds *int     `pulumi:"authorizerResultTtlInSeconds"`
	AuthorizerUri                *string  `pulumi:"authorizerUri"`
	IdentitySource               *string  `pulumi:"identitySource"`
	IdentityValidationExpression *string  `pulumi:"identityValidationExpression"`
	Name                         *string  `pulumi:"name"`
	ProviderARNs                 []string `pulumi:"providerARNs"`
	RestApiId                    string   `pulumi:"restApiId"`
	Type                         string   `pulumi:"type"`
}

// The set of arguments for constructing a Authorizer resource.
type AuthorizerArgs struct {
	AuthType                     pulumi.StringPtrInput
	AuthorizerCredentials        pulumi.StringPtrInput
	AuthorizerResultTtlInSeconds pulumi.IntPtrInput
	AuthorizerUri                pulumi.StringPtrInput
	IdentitySource               pulumi.StringPtrInput
	IdentityValidationExpression pulumi.StringPtrInput
	Name                         pulumi.StringPtrInput
	ProviderARNs                 pulumi.StringArrayInput
	RestApiId                    pulumi.StringInput
	Type                         pulumi.StringInput
}

func (AuthorizerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*authorizerArgs)(nil)).Elem()
}

type AuthorizerInput interface {
	pulumi.Input

	ToAuthorizerOutput() AuthorizerOutput
	ToAuthorizerOutputWithContext(ctx context.Context) AuthorizerOutput
}

func (*Authorizer) ElementType() reflect.Type {
	return reflect.TypeOf((*Authorizer)(nil))
}

func (i *Authorizer) ToAuthorizerOutput() AuthorizerOutput {
	return i.ToAuthorizerOutputWithContext(context.Background())
}

func (i *Authorizer) ToAuthorizerOutputWithContext(ctx context.Context) AuthorizerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AuthorizerOutput)
}

type AuthorizerOutput struct{ *pulumi.OutputState }

func (AuthorizerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Authorizer)(nil))
}

func (o AuthorizerOutput) ToAuthorizerOutput() AuthorizerOutput {
	return o
}

func (o AuthorizerOutput) ToAuthorizerOutputWithContext(ctx context.Context) AuthorizerOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AuthorizerOutput{})
}
