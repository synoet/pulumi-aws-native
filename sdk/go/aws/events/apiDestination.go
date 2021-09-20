// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package events

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Events::ApiDestination.
type ApiDestination struct {
	pulumi.CustomResourceState

	// The arn of the api destination.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The arn of the connection.
	ConnectionArn pulumi.StringOutput            `pulumi:"connectionArn"`
	Description   pulumi.StringPtrOutput         `pulumi:"description"`
	HttpMethod    ApiDestinationHttpMethodOutput `pulumi:"httpMethod"`
	// Url endpoint to invoke.
	InvocationEndpoint           pulumi.StringOutput `pulumi:"invocationEndpoint"`
	InvocationRateLimitPerSecond pulumi.IntPtrOutput `pulumi:"invocationRateLimitPerSecond"`
	// Name of the apiDestination.
	Name pulumi.StringPtrOutput `pulumi:"name"`
}

// NewApiDestination registers a new resource with the given unique name, arguments, and options.
func NewApiDestination(ctx *pulumi.Context,
	name string, args *ApiDestinationArgs, opts ...pulumi.ResourceOption) (*ApiDestination, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectionArn == nil {
		return nil, errors.New("invalid value for required argument 'ConnectionArn'")
	}
	if args.HttpMethod == nil {
		return nil, errors.New("invalid value for required argument 'HttpMethod'")
	}
	if args.InvocationEndpoint == nil {
		return nil, errors.New("invalid value for required argument 'InvocationEndpoint'")
	}
	var resource ApiDestination
	err := ctx.RegisterResource("aws-native:events:ApiDestination", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApiDestination gets an existing ApiDestination resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApiDestination(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApiDestinationState, opts ...pulumi.ResourceOption) (*ApiDestination, error) {
	var resource ApiDestination
	err := ctx.ReadResource("aws-native:events:ApiDestination", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ApiDestination resources.
type apiDestinationState struct {
}

type ApiDestinationState struct {
}

func (ApiDestinationState) ElementType() reflect.Type {
	return reflect.TypeOf((*apiDestinationState)(nil)).Elem()
}

type apiDestinationArgs struct {
	// The arn of the connection.
	ConnectionArn string                   `pulumi:"connectionArn"`
	Description   *string                  `pulumi:"description"`
	HttpMethod    ApiDestinationHttpMethod `pulumi:"httpMethod"`
	// Url endpoint to invoke.
	InvocationEndpoint           string `pulumi:"invocationEndpoint"`
	InvocationRateLimitPerSecond *int   `pulumi:"invocationRateLimitPerSecond"`
	// Name of the apiDestination.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a ApiDestination resource.
type ApiDestinationArgs struct {
	// The arn of the connection.
	ConnectionArn pulumi.StringInput
	Description   pulumi.StringPtrInput
	HttpMethod    ApiDestinationHttpMethodInput
	// Url endpoint to invoke.
	InvocationEndpoint           pulumi.StringInput
	InvocationRateLimitPerSecond pulumi.IntPtrInput
	// Name of the apiDestination.
	Name pulumi.StringPtrInput
}

func (ApiDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*apiDestinationArgs)(nil)).Elem()
}

type ApiDestinationInput interface {
	pulumi.Input

	ToApiDestinationOutput() ApiDestinationOutput
	ToApiDestinationOutputWithContext(ctx context.Context) ApiDestinationOutput
}

func (*ApiDestination) ElementType() reflect.Type {
	return reflect.TypeOf((*ApiDestination)(nil))
}

func (i *ApiDestination) ToApiDestinationOutput() ApiDestinationOutput {
	return i.ToApiDestinationOutputWithContext(context.Background())
}

func (i *ApiDestination) ToApiDestinationOutputWithContext(ctx context.Context) ApiDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApiDestinationOutput)
}

type ApiDestinationOutput struct{ *pulumi.OutputState }

func (ApiDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ApiDestination)(nil))
}

func (o ApiDestinationOutput) ToApiDestinationOutput() ApiDestinationOutput {
	return o
}

func (o ApiDestinationOutput) ToApiDestinationOutputWithContext(ctx context.Context) ApiDestinationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ApiDestinationOutput{})
}
