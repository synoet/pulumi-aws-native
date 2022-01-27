// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Lambda::Url
//
// Deprecated: Url is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Url struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the Function URL.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.
	AuthorizationType UrlAuthorizationTypeOutput `pulumi:"authorizationType"`
	Cors              UrlCorsPtrOutput           `pulumi:"cors"`
	// The generated url for this resource.
	FunctionUrl pulumi.StringOutput `pulumi:"functionUrl"`
	// The alias qualifier for the target function. If TargetFunctionArn is unqualified then Qualifier must be passed.
	Qualifier pulumi.StringPtrOutput `pulumi:"qualifier"`
	// The Amazon Resource Name (ARN) of the function associated with the Function URL.
	TargetFunctionArn pulumi.StringOutput `pulumi:"targetFunctionArn"`
}

// NewUrl registers a new resource with the given unique name, arguments, and options.
func NewUrl(ctx *pulumi.Context,
	name string, args *UrlArgs, opts ...pulumi.ResourceOption) (*Url, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AuthorizationType == nil {
		return nil, errors.New("invalid value for required argument 'AuthorizationType'")
	}
	if args.TargetFunctionArn == nil {
		return nil, errors.New("invalid value for required argument 'TargetFunctionArn'")
	}
	var resource Url
	err := ctx.RegisterResource("aws-native:lambda:Url", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUrl gets an existing Url resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUrl(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UrlState, opts ...pulumi.ResourceOption) (*Url, error) {
	var resource Url
	err := ctx.ReadResource("aws-native:lambda:Url", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Url resources.
type urlState struct {
}

type UrlState struct {
}

func (UrlState) ElementType() reflect.Type {
	return reflect.TypeOf((*urlState)(nil)).Elem()
}

type urlArgs struct {
	// Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.
	AuthorizationType UrlAuthorizationType `pulumi:"authorizationType"`
	Cors              *UrlCors             `pulumi:"cors"`
	// The alias qualifier for the target function. If TargetFunctionArn is unqualified then Qualifier must be passed.
	Qualifier *string `pulumi:"qualifier"`
	// The Amazon Resource Name (ARN) of the function associated with the Function URL.
	TargetFunctionArn string `pulumi:"targetFunctionArn"`
}

// The set of arguments for constructing a Url resource.
type UrlArgs struct {
	// Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.
	AuthorizationType UrlAuthorizationTypeInput
	Cors              UrlCorsPtrInput
	// The alias qualifier for the target function. If TargetFunctionArn is unqualified then Qualifier must be passed.
	Qualifier pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the function associated with the Function URL.
	TargetFunctionArn pulumi.StringInput
}

func (UrlArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*urlArgs)(nil)).Elem()
}

type UrlInput interface {
	pulumi.Input

	ToUrlOutput() UrlOutput
	ToUrlOutputWithContext(ctx context.Context) UrlOutput
}

func (*Url) ElementType() reflect.Type {
	return reflect.TypeOf((**Url)(nil)).Elem()
}

func (i *Url) ToUrlOutput() UrlOutput {
	return i.ToUrlOutputWithContext(context.Background())
}

func (i *Url) ToUrlOutputWithContext(ctx context.Context) UrlOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UrlOutput)
}

type UrlOutput struct{ *pulumi.OutputState }

func (UrlOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Url)(nil)).Elem()
}

func (o UrlOutput) ToUrlOutput() UrlOutput {
	return o
}

func (o UrlOutput) ToUrlOutputWithContext(ctx context.Context) UrlOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UrlInput)(nil)).Elem(), &Url{})
	pulumi.RegisterOutputType(UrlOutput{})
}
