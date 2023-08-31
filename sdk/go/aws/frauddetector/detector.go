// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package frauddetector

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A resource schema for a Detector in Amazon Fraud Detector.
type Detector struct {
	pulumi.CustomResourceState

	// The ARN of the detector.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The models to associate with this detector.
	AssociatedModels DetectorModelArrayOutput `pulumi:"associatedModels"`
	// The time when the detector was created.
	CreatedTime pulumi.StringOutput `pulumi:"createdTime"`
	// The description of the detector.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The ID of the detector
	DetectorId pulumi.StringOutput `pulumi:"detectorId"`
	// The active version ID of the detector
	DetectorVersionId pulumi.StringOutput `pulumi:"detectorVersionId"`
	// The desired detector version status for the detector
	DetectorVersionStatus DetectorVersionStatusPtrOutput `pulumi:"detectorVersionStatus"`
	// The event type to associate this detector with.
	EventType DetectorEventTypeOutput `pulumi:"eventType"`
	// The time when the detector was last updated.
	LastUpdatedTime   pulumi.StringOutput                `pulumi:"lastUpdatedTime"`
	RuleExecutionMode DetectorRuleExecutionModePtrOutput `pulumi:"ruleExecutionMode"`
	Rules             DetectorRuleArrayOutput            `pulumi:"rules"`
	// Tags associated with this detector.
	Tags DetectorTagArrayOutput `pulumi:"tags"`
}

// NewDetector registers a new resource with the given unique name, arguments, and options.
func NewDetector(ctx *pulumi.Context,
	name string, args *DetectorArgs, opts ...pulumi.ResourceOption) (*Detector, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DetectorId == nil {
		return nil, errors.New("invalid value for required argument 'DetectorId'")
	}
	if args.EventType == nil {
		return nil, errors.New("invalid value for required argument 'EventType'")
	}
	if args.Rules == nil {
		return nil, errors.New("invalid value for required argument 'Rules'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"detectorId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Detector
	err := ctx.RegisterResource("aws-native:frauddetector:Detector", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDetector gets an existing Detector resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDetector(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DetectorState, opts ...pulumi.ResourceOption) (*Detector, error) {
	var resource Detector
	err := ctx.ReadResource("aws-native:frauddetector:Detector", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Detector resources.
type detectorState struct {
}

type DetectorState struct {
}

func (DetectorState) ElementType() reflect.Type {
	return reflect.TypeOf((*detectorState)(nil)).Elem()
}

type detectorArgs struct {
	// The models to associate with this detector.
	AssociatedModels []DetectorModel `pulumi:"associatedModels"`
	// The description of the detector.
	Description *string `pulumi:"description"`
	// The ID of the detector
	DetectorId string `pulumi:"detectorId"`
	// The desired detector version status for the detector
	DetectorVersionStatus *DetectorVersionStatus `pulumi:"detectorVersionStatus"`
	// The event type to associate this detector with.
	EventType         DetectorEventType          `pulumi:"eventType"`
	RuleExecutionMode *DetectorRuleExecutionMode `pulumi:"ruleExecutionMode"`
	Rules             []DetectorRule             `pulumi:"rules"`
	// Tags associated with this detector.
	Tags []DetectorTag `pulumi:"tags"`
}

// The set of arguments for constructing a Detector resource.
type DetectorArgs struct {
	// The models to associate with this detector.
	AssociatedModels DetectorModelArrayInput
	// The description of the detector.
	Description pulumi.StringPtrInput
	// The ID of the detector
	DetectorId pulumi.StringInput
	// The desired detector version status for the detector
	DetectorVersionStatus DetectorVersionStatusPtrInput
	// The event type to associate this detector with.
	EventType         DetectorEventTypeInput
	RuleExecutionMode DetectorRuleExecutionModePtrInput
	Rules             DetectorRuleArrayInput
	// Tags associated with this detector.
	Tags DetectorTagArrayInput
}

func (DetectorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*detectorArgs)(nil)).Elem()
}

type DetectorInput interface {
	pulumi.Input

	ToDetectorOutput() DetectorOutput
	ToDetectorOutputWithContext(ctx context.Context) DetectorOutput
}

func (*Detector) ElementType() reflect.Type {
	return reflect.TypeOf((**Detector)(nil)).Elem()
}

func (i *Detector) ToDetectorOutput() DetectorOutput {
	return i.ToDetectorOutputWithContext(context.Background())
}

func (i *Detector) ToDetectorOutputWithContext(ctx context.Context) DetectorOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DetectorOutput)
}

type DetectorOutput struct{ *pulumi.OutputState }

func (DetectorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Detector)(nil)).Elem()
}

func (o DetectorOutput) ToDetectorOutput() DetectorOutput {
	return o
}

func (o DetectorOutput) ToDetectorOutputWithContext(ctx context.Context) DetectorOutput {
	return o
}

// The ARN of the detector.
func (o DetectorOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Detector) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The models to associate with this detector.
func (o DetectorOutput) AssociatedModels() DetectorModelArrayOutput {
	return o.ApplyT(func(v *Detector) DetectorModelArrayOutput { return v.AssociatedModels }).(DetectorModelArrayOutput)
}

// The time when the detector was created.
func (o DetectorOutput) CreatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Detector) pulumi.StringOutput { return v.CreatedTime }).(pulumi.StringOutput)
}

// The description of the detector.
func (o DetectorOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Detector) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The ID of the detector
func (o DetectorOutput) DetectorId() pulumi.StringOutput {
	return o.ApplyT(func(v *Detector) pulumi.StringOutput { return v.DetectorId }).(pulumi.StringOutput)
}

// The active version ID of the detector
func (o DetectorOutput) DetectorVersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *Detector) pulumi.StringOutput { return v.DetectorVersionId }).(pulumi.StringOutput)
}

// The desired detector version status for the detector
func (o DetectorOutput) DetectorVersionStatus() DetectorVersionStatusPtrOutput {
	return o.ApplyT(func(v *Detector) DetectorVersionStatusPtrOutput { return v.DetectorVersionStatus }).(DetectorVersionStatusPtrOutput)
}

// The event type to associate this detector with.
func (o DetectorOutput) EventType() DetectorEventTypeOutput {
	return o.ApplyT(func(v *Detector) DetectorEventTypeOutput { return v.EventType }).(DetectorEventTypeOutput)
}

// The time when the detector was last updated.
func (o DetectorOutput) LastUpdatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Detector) pulumi.StringOutput { return v.LastUpdatedTime }).(pulumi.StringOutput)
}

func (o DetectorOutput) RuleExecutionMode() DetectorRuleExecutionModePtrOutput {
	return o.ApplyT(func(v *Detector) DetectorRuleExecutionModePtrOutput { return v.RuleExecutionMode }).(DetectorRuleExecutionModePtrOutput)
}

func (o DetectorOutput) Rules() DetectorRuleArrayOutput {
	return o.ApplyT(func(v *Detector) DetectorRuleArrayOutput { return v.Rules }).(DetectorRuleArrayOutput)
}

// Tags associated with this detector.
func (o DetectorOutput) Tags() DetectorTagArrayOutput {
	return o.ApplyT(func(v *Detector) DetectorTagArrayOutput { return v.Tags }).(DetectorTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DetectorInput)(nil)).Elem(), &Detector{})
	pulumi.RegisterOutputType(DetectorOutput{})
}
