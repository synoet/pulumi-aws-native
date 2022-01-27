// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ivs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::IVS::Channel
type Channel struct {
	pulumi.CustomResourceState

	// Channel ARN is automatically generated on creation and assigned as the unique identifier.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Whether the channel is authorized.
	Authorized pulumi.BoolPtrOutput `pulumi:"authorized"`
	// Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.
	IngestEndpoint pulumi.StringOutput `pulumi:"ingestEndpoint"`
	// Channel latency mode.
	LatencyMode ChannelLatencyModePtrOutput `pulumi:"latencyMode"`
	// Channel
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// Channel Playback URL.
	PlaybackUrl pulumi.StringOutput `pulumi:"playbackUrl"`
	// Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: “” (recording is disabled).
	RecordingConfigurationArn pulumi.StringPtrOutput `pulumi:"recordingConfigurationArn"`
	// A list of key-value pairs that contain metadata for the asset model.
	Tags ChannelTagArrayOutput `pulumi:"tags"`
	// Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
	Type ChannelTypePtrOutput `pulumi:"type"`
}

// NewChannel registers a new resource with the given unique name, arguments, and options.
func NewChannel(ctx *pulumi.Context,
	name string, args *ChannelArgs, opts ...pulumi.ResourceOption) (*Channel, error) {
	if args == nil {
		args = &ChannelArgs{}
	}

	var resource Channel
	err := ctx.RegisterResource("aws-native:ivs:Channel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetChannel gets an existing Channel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetChannel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ChannelState, opts ...pulumi.ResourceOption) (*Channel, error) {
	var resource Channel
	err := ctx.ReadResource("aws-native:ivs:Channel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Channel resources.
type channelState struct {
}

type ChannelState struct {
}

func (ChannelState) ElementType() reflect.Type {
	return reflect.TypeOf((*channelState)(nil)).Elem()
}

type channelArgs struct {
	// Whether the channel is authorized.
	Authorized *bool `pulumi:"authorized"`
	// Channel latency mode.
	LatencyMode *ChannelLatencyMode `pulumi:"latencyMode"`
	// Channel
	Name *string `pulumi:"name"`
	// Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: “” (recording is disabled).
	RecordingConfigurationArn *string `pulumi:"recordingConfigurationArn"`
	// A list of key-value pairs that contain metadata for the asset model.
	Tags []ChannelTag `pulumi:"tags"`
	// Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
	Type *ChannelType `pulumi:"type"`
}

// The set of arguments for constructing a Channel resource.
type ChannelArgs struct {
	// Whether the channel is authorized.
	Authorized pulumi.BoolPtrInput
	// Channel latency mode.
	LatencyMode ChannelLatencyModePtrInput
	// Channel
	Name pulumi.StringPtrInput
	// Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: “” (recording is disabled).
	RecordingConfigurationArn pulumi.StringPtrInput
	// A list of key-value pairs that contain metadata for the asset model.
	Tags ChannelTagArrayInput
	// Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.
	Type ChannelTypePtrInput
}

func (ChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*channelArgs)(nil)).Elem()
}

type ChannelInput interface {
	pulumi.Input

	ToChannelOutput() ChannelOutput
	ToChannelOutputWithContext(ctx context.Context) ChannelOutput
}

func (*Channel) ElementType() reflect.Type {
	return reflect.TypeOf((**Channel)(nil)).Elem()
}

func (i *Channel) ToChannelOutput() ChannelOutput {
	return i.ToChannelOutputWithContext(context.Background())
}

func (i *Channel) ToChannelOutputWithContext(ctx context.Context) ChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ChannelOutput)
}

type ChannelOutput struct{ *pulumi.OutputState }

func (ChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Channel)(nil)).Elem()
}

func (o ChannelOutput) ToChannelOutput() ChannelOutput {
	return o
}

func (o ChannelOutput) ToChannelOutputWithContext(ctx context.Context) ChannelOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ChannelInput)(nil)).Elem(), &Channel{})
	pulumi.RegisterOutputType(ChannelOutput{})
}
