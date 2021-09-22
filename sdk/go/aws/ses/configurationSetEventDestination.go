// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ses

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SES::ConfigurationSetEventDestination
//
// Deprecated: ConfigurationSetEventDestination is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ConfigurationSetEventDestination struct {
	pulumi.CustomResourceState

	ConfigurationSetName pulumi.StringOutput                                    `pulumi:"configurationSetName"`
	EventDestination     ConfigurationSetEventDestinationEventDestinationOutput `pulumi:"eventDestination"`
}

// NewConfigurationSetEventDestination registers a new resource with the given unique name, arguments, and options.
func NewConfigurationSetEventDestination(ctx *pulumi.Context,
	name string, args *ConfigurationSetEventDestinationArgs, opts ...pulumi.ResourceOption) (*ConfigurationSetEventDestination, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConfigurationSetName == nil {
		return nil, errors.New("invalid value for required argument 'ConfigurationSetName'")
	}
	if args.EventDestination == nil {
		return nil, errors.New("invalid value for required argument 'EventDestination'")
	}
	var resource ConfigurationSetEventDestination
	err := ctx.RegisterResource("aws-native:ses:ConfigurationSetEventDestination", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfigurationSetEventDestination gets an existing ConfigurationSetEventDestination resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfigurationSetEventDestination(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigurationSetEventDestinationState, opts ...pulumi.ResourceOption) (*ConfigurationSetEventDestination, error) {
	var resource ConfigurationSetEventDestination
	err := ctx.ReadResource("aws-native:ses:ConfigurationSetEventDestination", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConfigurationSetEventDestination resources.
type configurationSetEventDestinationState struct {
}

type ConfigurationSetEventDestinationState struct {
}

func (ConfigurationSetEventDestinationState) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationSetEventDestinationState)(nil)).Elem()
}

type configurationSetEventDestinationArgs struct {
	ConfigurationSetName string                                           `pulumi:"configurationSetName"`
	EventDestination     ConfigurationSetEventDestinationEventDestination `pulumi:"eventDestination"`
}

// The set of arguments for constructing a ConfigurationSetEventDestination resource.
type ConfigurationSetEventDestinationArgs struct {
	ConfigurationSetName pulumi.StringInput
	EventDestination     ConfigurationSetEventDestinationEventDestinationInput
}

func (ConfigurationSetEventDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationSetEventDestinationArgs)(nil)).Elem()
}

type ConfigurationSetEventDestinationInput interface {
	pulumi.Input

	ToConfigurationSetEventDestinationOutput() ConfigurationSetEventDestinationOutput
	ToConfigurationSetEventDestinationOutputWithContext(ctx context.Context) ConfigurationSetEventDestinationOutput
}

func (*ConfigurationSetEventDestination) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationSetEventDestination)(nil))
}

func (i *ConfigurationSetEventDestination) ToConfigurationSetEventDestinationOutput() ConfigurationSetEventDestinationOutput {
	return i.ToConfigurationSetEventDestinationOutputWithContext(context.Background())
}

func (i *ConfigurationSetEventDestination) ToConfigurationSetEventDestinationOutputWithContext(ctx context.Context) ConfigurationSetEventDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationSetEventDestinationOutput)
}

type ConfigurationSetEventDestinationOutput struct{ *pulumi.OutputState }

func (ConfigurationSetEventDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationSetEventDestination)(nil))
}

func (o ConfigurationSetEventDestinationOutput) ToConfigurationSetEventDestinationOutput() ConfigurationSetEventDestinationOutput {
	return o
}

func (o ConfigurationSetEventDestinationOutput) ToConfigurationSetEventDestinationOutputWithContext(ctx context.Context) ConfigurationSetEventDestinationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ConfigurationSetEventDestinationOutput{})
}
